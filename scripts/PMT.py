import arcpy
arcpy.CheckOutExtension("spatial")
from arcpy import env
from arcpy.sa import *
arcpy.env.overwriteOutput = True


############ variables
myraster_temp = arcpy.GetParameterAsText(0)

threshold = float(arcpy.GetParameterAsText(1) )
use_train = arcpy.GetParameterAsText(2)	#"true"
positive_train = arcpy.GetParameterAsText(3)
negative_train = arcpy.GetParameterAsText(4)
positive_validation = arcpy.GetParameterAsText(5)
negative_validation = arcpy.GetParameterAsText(6)
outworkspace_temp = arcpy.GetParameterAsText(7)
num_of_classes = int(arcpy.GetParameterAsText(8))


if use_train =="true":
	if (positive_train =="") or (negative_train ==""):
		arcpy.AddError("you didn't set Positive or presence (training) or Negative or absence (training)\n if you dont want use training data uncheck 'Include training step'")
		import sys
		sys.exit(1)



#prepare excel writer
###########################
from xlwt import *
w = Workbook()

ws_validation = w.add_sheet('validation',cell_overwrite_ok=True)
ws_train = w.add_sheet('train',cell_overwrite_ok=True)

ws_train.write(0, 0, "Model(s)")
ws_validation.write(0, 0, "Model(s)")
myrow = 0


##########################
myraster_temp = myraster_temp.split(";")
import os




def getstat(myraster,what = "MINIMUM"):
	myraster_= arcpy.Describe(myraster)
	myraster = myraster_.catalogPath

	try:
		raster_st = arcpy.GetRasterProperties_management(myraster, what)
		temp1 = raster_st.getOutput(0)
		temp2 = temp1.replace(",", ".")
		raster_st = float(temp2)
		return raster_st


	except arcpy.ExecuteError: 
		msgs = arcpy.GetMessages(2) 
        	error_code = str(msgs).replace(":","").split(" ")[1]
		if error_code == "001100":
			arcpy.CalculateStatistics_management(myraster, "1", "1", "", "OVERWRITE", "")
			raster_st = arcpy.GetRasterProperties_management(myraster, what)
			temp1 = raster_st.getOutput(0)
			temp2 = temp1.replace(",", ".")
			raster_st = float(temp2)
			return raster_st







for myraster in myraster_temp:
	myraster = myraster.replace("'", "")
	arcpy.AddMessage("%s"%myraster)
	myraster_= arcpy.Describe(myraster)
	myraster = myraster_.catalogPath
	myraster_name = myraster_.baseName

	#### excel
	myrow += 1
	ws_train.write(myrow, 0, myraster)

	outworkspace = outworkspace_temp + "/" + myraster_name
	if not os.path.exists(outworkspace):
		os.makedirs(outworkspace)

	layer_outworkspace = outworkspace + "/layers"
	if not os.path.exists(layer_outworkspace):
		os.makedirs(layer_outworkspace)


	raster_min = getstat(myraster,what = "MINIMUM")

	raster_max = getstat(myraster,what = "MAXIMUM")

	raster_range = raster_max - raster_min
	threshold = (threshold * raster_range / 100.0) + raster_min


	whereClause = "VALUE >= " + str(threshold)
	try:
		inRaster = arcpy.sa.Con(Raster(myraster) > threshold, 1, 0)
	except:
		inRaster = Con(myraster, 1, 0, whereClause)
	inRaster.save(layer_outworkspace + "/Con_raster.tif")


#################################################################################################################
	import do_it
	if use_train == "true":
		m_t = do_it.do_it("t",myraster, inRaster, threshold, positive_train, negative_train, outworkspace)
		arcpy.AddMessage(outworkspace)
		#### excel
		mycol = 1
		ws_validation.write(myrow, 0, myraster)
		for x,y in enumerate(m_t.keys()):
	   	   if y != "mmm":
			ws_train.write(myrow, mycol, str(m_t[y]))
			ws_train.write(0, mycol, str(y))
			mycol += 1


		for x in m_t:
	   		if x != "mmm":
				arcpy.AddMessage("{0} = {1}".format(x,m_t[x]))
			arcpy.AddMessage("-"*22)


################################
	m_v = do_it.do_it("v",myraster, inRaster, threshold, positive_validation, negative_validation, outworkspace)

	#### excel
	mycol = 1
	for x,y in enumerate(m_v.keys()):
	   	   if y != "mmm":
			ws_validation.write(myrow, mycol, str(m_v[y]))
			ws_validation.write(0, mycol, str(y))
			mycol += 1
	if use_train != "true":
		m_t = {}
		for bbb in m_v.keys():
			m_t[bbb] = m_t.get(bbb, 0)


#########################################
	import reporter
	reporter.reporter(outworkspace,T=m_t["T"],tp=m_t["tp"],fp=m_t["fp"],tn=m_t["tn"],fn=m_t["fn"],tp_random=m_t["tp_random"],E=m_t["E"],efficiency=m_t["efficiency"],True_positive_rate=m_t["True_positive_rate"],false_positive_rate=m_t["false_positive_rate"],threat_score=m_t["threat_score"],equitable_threat_score=m_t["equitable_threat_score"],pierces_skill_score=m_t["pierces_skill_score"],hedke_skill_score=m_t["hedke_skill_score"],odds_ratio=m_t["odds_ratio"],odd_ratio_skill_score=m_t["odd_ratio_skill_score"],tss=m_t["tss"], p_obs=m_t["p_obs"], p_exp=m_t["p_exp"], kappa=m_t["kappa"],Tv=m_v["T"],tpv=m_v["tp"],fpv=m_v["fp"],tnv=m_v["tn"],fnv=m_v["fn"],tp_randomv=m_v["tp_random"],Ev=m_v["E"],efficiencyv=m_v["efficiency"],True_positive_ratev=m_v["True_positive_rate"],false_positive_ratev=m_v["false_positive_rate"],threat_scorev=m_v["threat_score"],equitable_threat_scorev=m_v["equitable_threat_score"],pierces_skill_scorev=m_v["pierces_skill_score"],hedke_skill_scorev=m_v["hedke_skill_score"],odds_ratiov=m_v["odds_ratio"],odd_ratio_skill_scorev=m_v["odd_ratio_skill_score"],tssv=m_v["tss"], p_obsv=m_v["p_obs"], p_expv=m_v["p_exp"], kappav=m_v["kappa"],TNR=m_t["TNR"],PPV=m_t["PPV"],miss_rate=m_t["miss_rate"],Misclassification_rate=m_t["Misclassification_rate"],FDR=m_t["FDR"],NPV=m_t["NPV"],FOR_=m_t["FOR_"],F_score=m_t["F_score"],MCC=m_t["MCC"],BM=m_t["BM"],MK=m_t["MK"],TNRv=m_v["TNR"],PPVv=m_v["PPV"],miss_ratev=m_v["miss_rate"],Misclassification_ratev=m_v["Misclassification_rate"],FDRv=m_v["FDR"],NPVv=m_v["NPV"],FOR_v=m_v["FOR_"],F_scorev=m_v["F_score"],MCCv=m_v["MCC"],BMv=m_v["BM"],MKv=m_v["MK"])
#########################################

	import SRC_
	if use_train == "true":
		area_of_validation = SRC_.SRC_(myraster,raster_min,raster_max,outworkspace,num_of_classes,positive_validation,"Prediction rate curve (PRC)","PRC")
		area_of_train = SRC_.SRC_(myraster,raster_min,raster_max,outworkspace,num_of_classes,positive_train,"Success rate curve (SRC)","SRC")
	else:
		area_of_validation = SRC_.SRC_(myraster,raster_min,raster_max,outworkspace,num_of_classes,positive_validation,"Prediction rate curve (PRC)","PRC")
		area_of_train = 0 

#########################################
	from pyroc import *

	if use_train == "true":
		rmm = m_t["mmm"]
		roc = ROCCalc(rmm,linestyle='bo-') #linestyle='bo-'
		roc.plot(outworkspace +'//ROC_t.png',title='ROC curve (in training step)') # create a plot of the ROC curve
		auc_t = roc.auc()
		#arcpy.AddMessage(roc.auc())



	rmm = m_v["mmm"]
	roc = ROCCalc(rmm,linestyle='bo-') #linestyle='bo-'
	roc.plot(outworkspace +'//ROC_v.png',title='ROC curve (in validation step)') # create a plot of the ROC curve
	auc_v = roc.auc()
	arcpy.AddMessage(roc.auc())

	if use_train == "true":
		stability_auc = auc_v / auc_t
		arcpy.AddMessage(stability_auc)


#w.save(outworkspace_temp + '/dates.xls')