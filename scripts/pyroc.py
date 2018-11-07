import warnings
import sets
import random

try:
	import pylab
except ImportError:
	pass

def random_mixture_model(pos_mu=.6,pos_sigma=.1,neg_mu=.4,neg_sigma=.1,size=200):
	pos = [(1,random.gauss(pos_mu,pos_sigma),) for x in xrange(size/2)]
	neg = [(-1,random.gauss(neg_mu,neg_sigma),) for x in xrange(size/2)]

	return pos+neg

def deduplicate_styles(rocs_list):
	"""Given a list of ROCCalc objects, checks for duplicate linestyles, and
	replaces duplicates with a random one. This needs to be more thoroughly-
	tested."""
	pref_styles = ['cx-','mx-','yx-','gx-','bx-','rx-']
	LINES = ['-','-.',':']
	POINTS = 'ov^>+xd'
	COLORS = 'bgrcmy'
	rand_ls = []
	for r in rocs_list:
		if r.linestyle not in rand_ls:
			rand_ls.append(r.linestyle)
		else:
			while True:
				if len(pref_styles) > 0:
					pstyle = pref_styles.pop()
					if pstyle not in rand_ls:
	 					r.linestyle = pstyle
	 					rand_ls.append(pstyle)
	 					break
	 			else:
	 				ls = ''.join(random.sample(COLORS,1)+random.sample(POINTS,1)+random.sample(LINES,1))
	 				if ls not in rand_ls:
	 					r.linestyle = ls
	 					rand_ls.append(ls)
	 					break

def plot_multiple_rocs_separate(l_roccalc,fname,title='',labels=None,equal_aspect=True):
	"""Plots multiple ROC charts as separate on the same canvas."""
	pylab.clf()
	pylab.title(title)
	for ix,r in enumerate(l_roccalc):
		ax = pylab.subplot(4,4,ix+1)
		pylab.ylim((0,1))
		pylab.xlim((0,1))
		ax.set_yticklabels([])
		ax.set_xticklabels([])		
		if equal_aspect:
			cax = pylab.gca()
			cax.set_aspect('equal')
		if labels is None: labels=['' for x in l_roccalc]
		pylab.text(0.2,0.1,labels[ix],fontsize=8)		
		ef_plot = pylab.plot([x[0] for x in r.derived_points],[y[1] for y in r.derived_points],'r-',linewidth=2)
	pylab.savefig(fname,format='png')


def plot_multiple_roc(l_roccalc,fname,title='',labels=None,include_baseline=False,equal_aspect=True):
	"""Plots multiple ROC curves on the same chart."""
	pylab.clf()
	pylab.ylim((0,1))
	pylab.xlim((0,1))
	pylab.xticks(pylab.arange(0,1.1,.1))
	pylab.yticks(pylab.arange(0,1.1,.1))
	pylab.grid(True)
	if equal_aspect:
		cax = pylab.gca()
		cax.set_aspect('equal')
	pylab.xlabel("1 - Specificity")
	pylab.ylabel("Sensitivity")
	pylab.title(title)
	if labels is None: labels=['' for x in l_roccalc]
	deduplicate_styles(l_roccalc)
	for ix,r in enumerate(l_roccalc):
		pylab.plot([x[0] for x in r.derived_points],[y[1] for y in r.derived_points],r.linestyle,linewidth=1,label=labels[ix])
	if include_baseline:
		pylab.plot([0.0,1.0],[0.0,1.0],'k-.',label="random")
	if labels is not None: pylab.legend(loc='lower right')
	pylab.savefig(fname,format='png')

def load_decision_function(path):
	fh = open(path,'r')
	reader = [x.strip().split() for x in fh.read().split('\n')]
	model_data = []
	for line in reader:
		if len(line) == 0: continue
		dfclass,dfval = line
		model_data.append((int(dfclass),float(dfval)))
	fh.close()
	return model_data
	
class ROCCalc():
	"""Class that generates an ROC curve.
	Data is in the following format: a list l of tuples t
	where:
		t[0] = 1 for positive class and t[0] = -1 for negative class
		t[1] = score
		t[2] = label.
	"""
	def __init__(self,data,step=0.01,linestyle='rx-'):
		"""Constructor takes the data, a step (between 0 and 1) with which to increment
		the dataset amount it uses per measurement and a matplotlib style string (note:
		ROCCalc is still usable w/o matplotlib, i.e. the AUC is still available, but plots
		cannot be generated). The data should be represented in the following format:
			A list l of tuples t (l=[t_0,t_1,...,t_m]) where:
			t[0] = 1 for positive class and 0 for negative class
			t[1] = a score (does not have to be bounded by -1 and 1)
			t[2] = any label (optional)
		"""
		self.data = sorted(data,lambda x,y: cmp(y[1],x[1]))		
		self.linestyle = linestyle		
		self.auc() # Seed initial points with default full ROC

	def plot(self,fname,title='',include_baseline=False,equal_aspect=True):
		"""Generates a plot of the ROC curve."""
		pylab.clf()
		pylab.plot([x[0] for x in self.derived_points],[y[1] for y in self.derived_points],self.linestyle)
		if include_baseline:
			pylab.plot([0.0,1.0],[0.0,1.0],'k-.')
		pylab.ylim((0,1))
		pylab.xlim((0,1))
		pylab.xticks(pylab.arange(0,1.1,.1))
		pylab.yticks(pylab.arange(0,1.1,.1))	
		pylab.grid(True)
		if equal_aspect:
			cax = pylab.gca()
			cax.set_aspect('equal')
		pylab.xlabel("1 - Specificity")
		pylab.ylabel("Sensitivity")
		pylab.title(title)
##################
		#pylab.figsize=(2, 2)
		#pylab.rcParams['figure.figsize'] = 50, 100
		####pylab.text(0.5, 0.5,'matplotlib', horizontalalignment='right',verticalalignment='center')

		textstr = 'AUC=%.3f'%(self.auc())

		props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

		pylab.text(0.60, 0.15, textstr, fontsize=14,verticalalignment='top', bbox=props)
##################
		pylab.savefig(fname,format='png', dpi=300,size=(1, 1))
	
	def confusion_matrix(self,threshold,do_print=False):
		"""Returns the confusion matrix (in dictionary form) for a given threshold
		(where all elements > threshold are considered 1, all else 0)."""
		pos_data = [x for x in self.data if x[1] >= threshold]
		neg_data = [x for x in self.data if x[1] < threshold]
		tp,fp,fn,tn = self._calc_counts(pos_data,neg_data)
		if do_print:
			print "\tActual class"
			print "\t+(1)\t-(0)"
			print "+(1)\t%i\t%i\tPredicted"%(tp,fp)
			print "-(0)\t%i\t%i\tclass"%(fn,tn)
		return {'TP':tp,'FP':fp,'FN':fn,'TN':tn}
	
	def auc(self,fpnum=0):
		"""Uses trapezoidal rule to calculate the area under the curve. If fpnum is supplied, it will
		calculate a partial AUC, up to the number of false positives in fpnum (the partial AUC is scaled
		to between 0 and 1)."""
		return self._aucn(fpnum)
		
	def _aucn(self,fps):
		"""Uses a trapezoidal rule to calculate the area under the curve, up to a specified false positive count.
		This function essentially removes all instances past those of the cumulative FP count specified (fps), and calculates
		the individual points for each FP count (and as such, can be quite expensive for high fps).
		The function also assumes that the positive class is expected to have the higher of the scores (~s(+) > ~s(-))."""
		fps_count = 0
		relevant_pauc = []
		curindex = 0
		max_n = len([x for x in self.data if x[0] == -1])
		if fps == 0:
			relevant_pauc = [x for x in self.data]
		elif fps > max_n:
			fps = max_n
		# Find the upper limit of the data that does not exceed n FPs
		else:
			while fps_count < fps:
				relevant_pauc.append(self.data[curindex])
				if self.data[curindex][0] == -1:
					fps_count += 1
				curindex += 1
		total_n = len([x for x in relevant_pauc if x[0] == -1])
		total_p = len(relevant_pauc) - total_n
		# Convert to points in an ROC
		prev_df = -1000000.0
		curindex = 0
		points = []
		tp_count,fp_count = 0.0,0.0
		tpr,fpr = 0,0
		while curindex < len(relevant_pauc):
			df = relevant_pauc[curindex][1]
			if prev_df != df:
				points.append((fpr,tpr,fp_count))
			if relevant_pauc[curindex][0] == -1:
				fp_count += 1
			elif relevant_pauc[curindex][0] == 1:
				tp_count += 1
			fpr = fp_count/total_n
			tpr = tp_count/total_p
			prev_df = df
			curindex += 1
		points.append((fpr,tpr,fp_count)) # Add last point
		points.sort(key=lambda i: (i[0],i[1]))
		self.derived_points = points
		return self._trapezoidal_rule(points)
	
	def write_decision_function(self,writable):
		"""Write the decision function to the specified stream."""
		for x in self.data:
			writable.write('\t'.join(list([str(y) for y in x])))
			writable.write('\n')
	
	def _trapezoidal_rule(self,curve_pts):
		"""It's a trap!"""
		cum_area = 0.0
		for ix,x in enumerate(curve_pts[0:-1]):
			cur_pt = x
			next_pt = curve_pts[ix+1]
			cum_area += ((cur_pt[1]+next_pt[1])/2.0) * (next_pt[0]-cur_pt[0])
		return cum_area
	
	def _calc_counts(self,pos_data,neg_data):
		tp_count = len([x for x in pos_data if x[0] == 1])
		fp_count = len([x for x in pos_data if x[0] == -1])
		fn_count = len([x for x in neg_data if x[0] == 1])
		tn_count = len([x for x in neg_data if x[0] == -1])
		return tp_count,fp_count,fn_count,tn_count		

if __name__ == '__main__':
	from optparse import OptionParser

	parser = OptionParser()
	parser.add_option('-f','--file',dest='fpath',help='Path to a file with the class and decision function. The first column of each row is the class, and the second the decision score.')
	parser.add_option('-n','--max fp',dest='fp_n',default=0,help='Maximum false positives to calculate up to (for partial AUC).')
	parser.add_option('-p','--plot',dest='ppath',help='Path to write a png of the ROC to (matplotlib required).')
	parser.add_option('-d','--dots',action='store_true',dest='plotdots',default=False,help='Prints the x and y coordinates of the ROC to the standard out.')
	parser.add_option('-t','--title',dest='ptitle',default='',help='Title of plot.')
	
	(options,args) = parser.parse_args()
	
	try:
		df_data = load_decision_function(options.fpath)
		roc = ROCCalc(df_data)
		roc_n = int(options.fp_n)
		print roc.auc(roc_n)
		if options.ppath is not None:
			roc.plot(options.ppath,title=options.ptitle)
		if options.plotdots:
			print ''
			for pt in roc.derived_points:
				print pt[0],pt[1]
	except TypeError:
		parser.print_help()