import arcpy
arcpy.CheckOutExtension("spatial")
from arcpy import env
from arcpy.sa import *

arcpy.env.overwriteOutput = True
def do_it(mode_r,myraster, inRaster, threshold, positive_F, negative_F, outworkspace):
	field = "RASTERVALU"
	count = {}
	positive_list = []
	negative_list = []
	layer_outworkspace = outworkspace + "/layers"
	pos_f_ext = layer_outworkspace + "/pos_f_ext_%s.shp"%mode_r
	neg_f_ext = layer_outworkspace + "/neg_f_ext_%s.shp"%mode_r

	arcpy.AddMessage(pos_f_ext)
	arcpy.AddMessage(neg_f_ext)

	arcpy.sa.ExtractValuesToPoints(positive_F, inRaster, pos_f_ext,"INTERPOLATE", "VALUE_ONLY")
	arcpy.sa.ExtractValuesToPoints(negative_F, inRaster, neg_f_ext,"INTERPOLATE", "VALUE_ONLY")

	inRasterList = [[myraster, "myrasterv"]]

	ExtractMultiValuesToPoints(pos_f_ext, inRasterList, "BILINEAR")
	ExtractMultiValuesToPoints(neg_f_ext, inRasterList, "BILINEAR")


	mmm = []

	field = [field,"myrasterv"]

	with arcpy.da.SearchCursor(pos_f_ext,field) as cursor:
		for row in cursor:
			positive_list.append(row[0])
			mmm.append((1,row[1]),)

	with arcpy.da.SearchCursor(neg_f_ext,field) as cursor:
		for row in cursor:
			negative_list.append(row[0])
			mmm.append((-1,row[1]),)

	T = float(len(negative_list) + len(positive_list))

	tp = float(positive_list.count(1))
	fp = float(positive_list.count(0))

	tn = float(negative_list.count(0))
	fn = float(negative_list.count(1))


	tp_random = (tp + fn)*(tp + fp) / T
	E = ((tp + fn)*(tp + fp) + (tn + fn)*(tn + fp)) / T
	############################
	arcpy.AddMessage("tp=%s"%tp)
	arcpy.AddMessage("tn=%s"%tn)
	arcpy.AddMessage("fp=%s"%fp)
	arcpy.AddMessage("fn=%s"%fn)

	try:
		efficiency = (tp + tn) / T
	except:
		efficiency = 0

	try:
		True_positive_rate = tp / (tp + fn)
	except:
		True_positive_rate = 0

	TPR = True_positive_rate
	try:
		false_positive_rate = fp / (fp + tn)
	except:
		false_positive_rate = 0

	try:
		threat_score = tp / (tp + fn + fp)
	except:
		threat_score  = 0

	try:
		equitable_threat_score = (tp - tp_random) / (tp + fn + fp - tp_random)
	except:
		equitable_threat_score = 0
#
	try:
		pierces_skill_score = (tp / (tp + fn)) - ( fp / (fp + tn))
	except:
		pierces_skill_score = 0
#
	try:
		hedke_skill_score = (tp + tn - E) / (T - E)
	except:
		hedke_skill_score = 0
#
	try:
		odds_ratio = (tp * tn) / (fn * fp)
	except:
		odds_ratio = 0
#
	try:
		odd_ratio_skill_score = ((tp * tn) - (fp * fn)) / ((tn * tp) + (fp * fn))
	except:
		odd_ratio_skill_score = 0

	#True_positive_rate = tp / (tp + fn)
	#false_positive_rate = fp / (fp + tn)
	#threat_score = tp / (tp + fn + fp)
	#equitable_threat_score = (tp - tp_random) / (tp + fn + fp - tp_random)
	#pierces_skill_score = (tp / (tp + fn)) - ( fp / (fp + tn))
	#hedke_skill_score = (tp + tn - E) / (T - E)
	#odds_ratio = (tp * tn) / (fn * fp)
	#odd_ratio_skill_score = ((tp * tn) - (fp * fn)) / ((fn * fp) + (fp * fn))


	tss = True_positive_rate - false_positive_rate

	try:
		p_obs = (tp+tn)/(tp+fp+tn+fn)
	except:
		p_obs = 0

	try:
		p_exp = ((tp+fp)*(tp+fn)/((tp+fp+tn+fn)**2)) +((tn+fp)*(tn+fn)/((tp+fp+tn+fn)**2))
	except:
		p_exp = 0
	
	try:
		kappa = (p_obs - p_exp)/(1 - p_exp)
	except:
		kappa = 0
#############################################################################

	try:
		TNR = (tn)/(tn+fp)
	except:
		TNR = 0

	try:
		miss_rate = 1 - True_positive_rate
	except:
		miss_rate = 0


	try:
		Misclassification_rate = (fp + fn) / T
	except:
		Misclassification_rate = 0

	try:
		PPV = (tp) / (tp + fp)
	except:
		PPV = 0

	try:
		FDR = (fp) / (tp + fp)
	except:
		FDR = 0


	try:
		NPV = (tn) / (tn + fn)
	except:
		NPV = 0

	try:
		FOR_= (fn) / (tn + fn)
	except:
		FOR_ = 0

	try:
		F_score = (2*tp) / (2*tp + fp + fn)
	except:
		F_score = 0


	try:
		MCC = ((tp * tn) - (fp * fn)) / (((tp + fp)*(tp + fn)*(tn + fp)*(tn + fn))**0.5)
	except:
		MCC = 0

	try:
		BM = TPR + TNR - 1
	except:
		BM = 0


	try:
		MK = PPV + NPV - 1
	except:
		MK = 0








	return({"T":T,"tp":tp,"fp":fp,"tn":tn,"fn":fn,"tp_random":tp_random,"E":E,"efficiency":efficiency,"True_positive_rate":True_positive_rate,"false_positive_rate":false_positive_rate,"threat_score":threat_score,"equitable_threat_score":equitable_threat_score,"pierces_skill_score":pierces_skill_score,"hedke_skill_score":hedke_skill_score,"odds_ratio":odds_ratio,"odd_ratio_skill_score":odd_ratio_skill_score,"tss":tss, "p_obs":p_obs, "p_exp":p_exp, "kappa":kappa, "mmm":mmm, 'TNR':TNR, 'miss_rate':miss_rate,'Misclassification_rate':Misclassification_rate,'PPV':PPV,'FDR':FDR,'NPV':NPV,'FOR_':FOR_,'F_score':F_score,'MCC':MCC,'BM':BM,'MK':MK})








