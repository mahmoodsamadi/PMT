import arcpy
arcpy.CheckOutExtension("spatial")
from arcpy import env
from arcpy.sa import *

arcpy.env.overwriteOutput = True
def plot(x=None,y=None,area=None,fname=None,title='',include_baseline=False,equal_aspect=True,linestyle='r--'): #linestyle='rx-'
		import pylab
		pylab.clf()
		pylab.plot(x,y,linestyle)
		pylab.grid(True)

		pylab.xlabel("percentage of the area")
		pylab.ylabel("percentage of occurrences")
		pylab.title(title)

		#pylab.ylim((0,100))
		#pylab.xlim((0,100))

		textstr = 'AUC=%.3f'%(area)
		props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
		##pylab.text(70, min(y)+5, textstr, fontsize=14,verticalalignment='top', bbox=props)
		pylab.text(70, min(y)+15, textstr, fontsize=14,verticalalignment='top', bbox=props)
		pylab.savefig(fname,format='png', dpi=300,size=(1, 1))

def SRC_(myraster,raster_min,raster_max,outworkspace,class_num,event_layer,title,out_name):
	#!!!	reclassing
	layer_outworkspace = outworkspace + "/layers"
	myrange = (raster_max - raster_min) / class_num
	mm = []
	min_ = raster_min
	min_ = float('{0:.3f}'.format(min_))

	#min_ = int(min_)
	for x in range(class_num):
		mm.append([min_,min_ + myrange, x])
		min_ = min_ + myrange

	reclassed_raster = layer_outworkspace + "/reclassed"
	outReclass2 = arcpy.sa.Reclassify(Raster(myraster), "Value", RemapRange(mm))
	outReclass2.save(reclassed_raster)

	#!!!	pixels in classes
	class_pixels_count = {}
	my_table = arcpy.BuildRasterAttributeTable_management(outReclass2,"Overwrite")

	with arcpy.da.SearchCursor(my_table,["VALUE","COUNT"]) as cursor:
		for row in cursor:
			class_pixels_count[row[0]] = row[1]
	total_area = 0
	for x in class_pixels_count:
		#arcpy.AddMessage(class_pixels_count.get(x,0))
		total_area += class_pixels_count.get(x,0)

	#!!!	events in each classes

	class_field_name = "class_name"
	try:
		arcpy.DeleteField_management(event_layer,[class_field_name])
	except:
		pass

	inRasterList = [[outReclass2, class_field_name]]
	ExtractMultiValuesToPoints(event_layer , inRasterList, "BILINEAR")
	p_events_in_classes = []
	field = [class_field_name]
	with arcpy.da.SearchCursor(event_layer,field) as cursor:
		for row in cursor:
			p_events_in_classes.append(row[0])


	#arcpy.AddMessage("-"*33)
	#for x in p_events_in_classes:
	#	arcpy.AddMessage(x)
	#arcpy.AddMessage("-"*33)
	#arcpy.AddMessage(len(p_events_in_classes))
	total_events = len(p_events_in_classes)
	class_info = {}
	for x in range(class_num):
		#arcpy.AddMessage(str(x))
		#arcpy.AddMessage(str(class_pixels_count.get(x,0)))
		#arcpy.AddMessage(str(p_events_in_classes.count(x)))
		class_info[x] = (class_pixels_count.get(x,0),p_events_in_classes.count(x))
		#arcpy.AddMessage("class: %s,class count:%s,ps count:%s"%(x,class_pixels_count[x],p_events_in_classes.count(x)))


	area = 0
	area_perc_acc = [0]
	events = 0
	events_perc_acc = [0]
	for x in range(class_num - 1,-1,-1):
		area1 = class_info[x][0]
		#arcpy.AddMessage(area1)
		area1 = float(area1) / float(total_area) * 100
		area = area + area1
		area_perc_acc.append(area)
		#arcpy.AddMessage(area)

		events1 = class_info[x][1]
		#arcpy.AddMessage(events1)
		events1 = float(events1) / float(total_events) * 100
		events = events + events1
		events_perc_acc.append(events)
		#arcpy.AddMessage(events)


	#arcpy.AddMessage(area_perc_acc)
	#arcpy.AddMessage(events_perc_acc)

	## area under curve

	events = 0
	areas = 0
	sum = 0
	for s in range(len(area_perc_acc)):
		gg = (events + events_perc_acc[s]) / 2 * (area_perc_acc[s] - areas)
		sum += gg
		areas = area_perc_acc[s]
		events = events_perc_acc[s]
	area_under_curve = sum / 100

	#arcpy.AddMessage(area_perc_acc)

	import matplotlib.pyplot as plt
	x = area_perc_acc
	y = events_perc_acc
	#plt.plot(x,y)
	#plt.savefig(outworkspace + "/%s.png"%out_name,format='png', dpi=300,size=(1, 1))


	plot(x=x,y=y,area = area_under_curve,fname = outworkspace + "/%s.png"%out_name,title = title)

	return area