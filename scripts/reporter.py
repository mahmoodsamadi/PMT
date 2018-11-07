def reporter(outworkspace,T,tp,fp,tn,fn,tp_random,E,efficiency,True_positive_rate,false_positive_rate,threat_score,equitable_threat_score,pierces_skill_score,hedke_skill_score,odds_ratio,odd_ratio_skill_score,tss, p_obs, p_exp, kappa,Tv,tpv,fpv,tnv,fnv,tp_randomv,Ev,efficiencyv,True_positive_ratev,false_positive_ratev,threat_scorev,equitable_threat_scorev,pierces_skill_scorev,hedke_skill_scorev,odds_ratiov,odd_ratio_skill_scorev,tssv, p_obsv, p_expv, kappav,TNR,PPV,miss_rate,Misclassification_rate,FDR,NPV,FOR_,F_score,MCC,BM,MK,TNRv,PPVv,miss_ratev,Misclassification_ratev,FDRv,NPVv,FOR_v,F_scorev,MCCv,BMv,MKv):
#def reporter(outworkspace,T,tp,fp,tn,fn,tp_random,E,efficiency,True_positive_rate,false_positive_rate,threat_score,equitable_threat_score,pierces_skill_score,hedke_skill_score,odds_ratio,odd_ratio_skill_score,tss, p_obs, p_exp, kappa,Tv,tpv,fpv,tnv,fnv,tp_randomv,Ev,efficiencyv,True_positive_ratev,false_positive_ratev,threat_scorev,equitable_threat_scorev,pierces_skill_scorev,hedke_skill_scorev,odds_ratiov,odd_ratio_skill_scorev,tssv, p_obsv, p_expv, kappav,TNR,miss_rate,Misclassification_rate,FDR,NPV,FOR_,F_score,MCC,BM,MK,TNRv,miss_ratev,Misclassification_ratev,FDRv,NPVv,FOR_v,F_scorev,MCCv,BMv,MKv,):
	
	style = "table.GeneratedTable {width: 40%;background-color: #ffffff;border-collapse: collapse;border-width: 2px;border-color: #b649ad;border-style: solid;color: #000000;}table.GeneratedTable td, table.GeneratedTable th {text-align: center;border-width: 2px;border-color: #b649ad;border-style: solid;padding: 3px;}table.GeneratedTable thead {background-color: #ffcc00;}"

	html = """
 <!DOCTYPE html>
<html>
<head>
<title>Report</title>

<style>
{style}
</style>
</head>
<body>
<center>
<h2>
Assesment of model(s) accuracy using different threshold-dependent and threshold-independent performance measures
</h2>
</center>
<p>
The process of accuracy assessment includes the assessment of good-ness of fit (i.e., degree of fitting), and predictive performance (prediction skills) of the models using training and validation datasets, respectively. Different threshold-dependent and threshold-independent evaluation criteria represented below which are both groups based on a confusion matrix.
</p>
<br>
<h3>Confusion matrix</h3>
<p>
In order to represent a confusion matrix (also known as contingency table), we should compare observed data and model results. It is always based on true positives (TP), true negatives (TN), false positives (FP), and false negatives (FN). In general, false positive and false negatives have been known as Error Type I and Error Type II, respectively.
</p><br>
<center>
<p>
Confusion matrix used for evaluation of models.
</p>
<!--#########################################-->


<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none;background-color:#aeb6bf'>
 <tr>
  <td width=260 valign=top style='width:155.8pt;border:none;border-top:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Observed</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Predicted</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td width=260 valign=top style='width:155.8pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>&nbsp;</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Non-occurrence (&#8722;)</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Occurrence (+)</p>
  </td>
 </tr>
 <tr>
  <td width=260 valign=top style='width:155.8pt;border:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Non-occurrence (&#8722;)</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>(&#8722;|&#8722;) True negative (TN)</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>(+|&#8722;) false positive (FP)</p>
  </td>
 </tr>
 <tr>
  <td width=260 valign=top style='width:155.8pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Occurrence (+)</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>(&#8722;|+) false negative (FN)</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>(+|+) True positive (TP)</p>
  </td>
 </tr>
</table>
</center>


<br>
<br>
<center>
<p>
Contingency matrix of training step.
</p>
<!--#########################################-->

<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none;background-color:#aeb6bf'>
 <tr>
  <td width=260 valign=top style='width:155.8pt;border:none;border-top:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Observed</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Predicted</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td width=260 valign=top style='width:155.8pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>&nbsp;</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Non-occurrence (&#8722;)</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Occurrence (+)</p>
  </td>
 </tr>
 <tr>
  <td width=260 valign=top style='width:155.8pt;border:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Non-occurrence (&#8722;)</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>{tn}</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>{fp}</p>
  </td>
 </tr>
 <tr>
  <td width=260 valign=top style='width:155.8pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Occurrence (+)</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>{fn}</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>{tp}</p>
  </td>
 </tr>
</table>
</center>

<br>
<br>
<center>
<p>
Contingency matrix of validation step
</p>
<!--#########################################-->


<table class=MsoTableGrid border=1 cellspacing=0 cellpadding=0
 style='border-collapse:collapse;border:none;background-color:#aeb6bf'>
 <tr>
  <td width=260 valign=top style='width:155.8pt;border:none;border-top:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Observed</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Predicted</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border-top:solid windowtext 1.0pt;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:none;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>&nbsp;</p>
  </td>
 </tr>
 <tr>
  <td width=260 valign=top style='width:155.8pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>&nbsp;</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Non-occurrence (&#8722;)</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Occurrence (+)</p>
  </td>
 </tr>
 <tr>
  <td width=260 valign=top style='width:155.8pt;border:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Non-occurrence (&#8722;)</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>{tnv}</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>{fpv}</p>
  </td>
 </tr>
 <tr>
  <td width=260 valign=top style='width:155.8pt;border:none;border-bottom:solid windowtext 1.0pt;
  padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>Occurrence (+)</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>{fnv}</p>
  </td>
  <td width=260 valign=top style='width:155.85pt;border:none;border-bottom:
  solid windowtext 1.0pt;padding:0cm 5.4pt 0cm 5.4pt'>
  <p class=MsoNormal style='margin-bottom:0cm;margin-bottom:.0001pt;line-height:
  normal'>{tpv}</p>
  </td>
 </tr>
</table>
</center>

<hr>
<br>
<h3>Threshold-dependent criteria</h3>
<p>
There are some threshold-dependent criteria which were calculated based on the components of contingency table and also need a threshold for classifying the result map into two class: stable and unstable. These evaluation criteria are: Efficiency, True positive rate, false positive rate, Threat score, Equitable threat score, Pierces skill score, Hedke skill score, Odds ratio, Odd ratio skill score, True skill statistic (TSS) (also known as Pierce's skill score or Informedness) and Cohen's kappa.
</p><br>
<center>
<p>
Predictive performance of model(s) based on different threshold-dependent criteria in both training and validation steps.
</p>
<!--#########################################-->


<table class="GeneratedTable">
  <thead>
    <tr>
      <th>Accuracy statistics</th>
      <th>Training step</th>
      <th>Validation step</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Efficiency (accuracy)</td>
      <td>{efficiency:.4f}</td>
      <td>{efficiencyv:.4f}</td>
    </tr>
    <tr>
      <td>True positive rate (TPR; sensitivity)</td>
      <td>{True_positive_rate:.4f}</td>
      <td>{True_positive_ratev:.4f}</td>
    </tr>

    <tr>
      <td>False positive rate (FPR; fall-out; 1-specificity)</td>
      <td>{false_positive_rate:.4f}</td>
      <td>{false_positive_ratev:.4f}</td>
    </tr>
    <tr>
      <td>Threat score</td>
      <td>{threat_score:.4f}</td>
      <td>{threat_scorev:.4f}</td>
    </tr>
    <tr>
      <td>Equitable threat score</td>
      <td>{equitable_threat_score:.4f}</td>
      <td>{equitable_threat_scorev:.4f}</td>
    </tr>

    <tr>
      <td>Hedke skill score</td>
      <td>{hedke_skill_score:.4f}</td>
      <td>{hedke_skill_scorev:.4f}</td>
    </tr>
    <tr>
      <td>Odds ratio</td>
      <td>{odds_ratio:.4f}</td>
      <td>{odds_ratiov:.4f}</td>
    </tr>
    <tr>
      <td>Odd ratio skill score</td>
      <td>{odd_ratio_skill_score:.4f}</td>
      <td>{odd_ratio_skill_scorev:.4f}</td>
    </tr>
    <tr>
      <td>True skill statistic (Pierce's skill score)</td>
      <td>{tss:.4f}</td>
      <td>{tssv:.4f}</td>
    </tr>
    <tr>
      <td>Cohen's kappa</td>
      <td>{kappa:.4f}</td>
      <td>{kappav:.4f}</td>
    </tr>

    <tr>
      <td>True negative rate (TNR; specificity)</td>
      <td>{TNR:.4f}</td>
      <td>{TNRv:.4f}</td>
    </tr>

    <tr>
      <td>False negative rate (miss rate)</td>
      <td>{miss_rate:.4f}</td>
      <td>{miss_ratev:.4f}</td>
    </tr>

    <tr>
      <td>Misclassification rate</td>
      <td>{Misclassification_rate:.4f}</td>
      <td>{Misclassification_ratev:.4f}</td>
    </tr>

    <tr>
      <td>Positive predictive value (PPV; precision)</td>
      <td>{PPV:.4f}</td>
      <td>{PPVv:.4f}</td>
    </tr>

    <tr>
      <td>False discovery rate (FDR)</td>
      <td>{FDR:.4f}</td>
      <td>{FDRv:.4f}</td>
    </tr>

    <tr>
      <td>Negative predictive value (NPV)</td>
      <td>{NPV:.4f}</td>
      <td>{NPVv:.4f}</td>
    </tr>

    <tr>
      <td>False omission rate (FOR)</td>
      <td>{FOR_:.4f}</td>
      <td>{FOR_v:.4f}</td>
    </tr>

    <tr>
      <td>F-score</td>
      <td>{F_score:.4f}</td>
      <td>{F_scorev:.4f}</td>
    </tr>

    <tr>
      <td>Matthews correlation coefficient (MCC)</td>
      <td>{MCC:.4f}</td>
      <td>{MCCv:.4f}</td>
    </tr>

    <tr>
      <td>Informedness (Bookmaker informedness; BM)</td>
      <td>{BM:.4f}</td>
      <td>{BMv:.4f}</td>
    </tr>

    <tr>
      <td>Markedness (MK)</td>
      <td>{MK:.4f}</td>
      <td>{MKv:.4f}</td>
    </tr>

  </tbody>
</table>
</center>


<hr>
<br>
<h3>Threshold-independent criteria</h3>
<h4>1- Receiver operating characteristic (ROC) curve.</h4>
<p>
The ROC curve is a graph based on the sensitivity and 1 - specificity with various cut-off thresholds, which in order to assess the prediction accuracy quantitatively. These rates explain how well the model and predictive factors predict the phenomenon (e.g., landslide, flood). So, the area under the ROC curves (AUC) can be considered as the statistical summary of the overall performance. The AUC is commonly recognized as the most useful accuracy statistic in spatial modeling.
</p><br>
<center>
<p>
ROC curves and their AUC values in both training and validation steps.
</p>
<!--#########################################-->


<table class="GeneratedTable">
  <thead>
    <tr>
      <th>Training step</th>
      <th>Validation step</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="ROC_t.png"><img src="ROC_t.png"  width="99%" /></a></td>
      <td><a href="ROC_v.png"><img src="ROC_v.png"  width="99%" /></a></td>
    </tr>
  </tbody>
</table>
</center>


<br>
<h4>2- Success rate curve (SRC) and prediction rate curve (PRC).</h4>
<p>
The SRC and PRC curves determine the percentage of phenomenon (e.g., flood) in each probability category. The SRC is produced by comparing a susceptibility map with the training dataset, although the PRC considers the mentioned susceptibility map with validation dataset. These curves are created by plotting the cumulative percentage of susceptible areas (e.g., flood susceptible areas) on the x axis and the cumulative percentage of phenomenon events (e.g., flood) on the y axis. The steeper curve represents that the more number of phenomenon events fall into the most susceptible categories.
<br>The SRC shows how well the model could fit to the training dataset. The prediction ability of the model cannot be determined by SRC curve, because it is produced by phenomenon pixels that have already been utilized for constructing the model. Since the PRC curve is created by comparing a susceptibility map (e.g., flood susceptibility map) with phenomenon (e.g., flood) validation dataset, it can be used to evaluate the prediction ability of the model.
</p><br>
<center>
<p>
SRC and PRC curves and their AUC values.
</p>
<!--#########################################-->

<table class="GeneratedTable">
  <thead>
    <tr>
      <th>Training step</th>
      <th>Validation step</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="SRC.png"><img src="SRC.png"  width="99%" /></a></td>
      <td><a href="PRC.png"><img src="PRC.png"  width="99%" /></a></td>
    </tr>
  </tbody>
</table>
</center>
</body>
</html> 

	""".format(style = style,T=T,tp=tp,fp=fp,tn=tn,fn=fn,tp_random=tp_random,E=E,efficiency=efficiency,True_positive_rate=True_positive_rate,false_positive_rate=false_positive_rate,threat_score=threat_score,equitable_threat_score=equitable_threat_score,pierces_skill_score=pierces_skill_score,hedke_skill_score=hedke_skill_score,odds_ratio=odds_ratio,odd_ratio_skill_score=odd_ratio_skill_score,tss=tss, p_obs=p_obs, p_exp=p_exp, kappa=kappa,Tv=Tv,tpv=tpv,fpv=fpv,tnv=tnv,fnv=fnv,tp_randomv=tp_randomv,Ev=Ev,efficiencyv=efficiencyv,True_positive_ratev=True_positive_ratev,false_positive_ratev=false_positive_ratev,threat_scorev=threat_scorev,equitable_threat_scorev=equitable_threat_scorev,pierces_skill_scorev=pierces_skill_scorev,hedke_skill_scorev=hedke_skill_scorev,odds_ratiov=odds_ratiov,odd_ratio_skill_scorev=odd_ratio_skill_scorev,tssv=tssv, p_obsv=p_obsv, p_expv=p_expv, kappav=kappav,TNR=TNR,PPV = PPV,miss_rate=miss_rate,Misclassification_rate=Misclassification_rate,FDR=FDR,NPV=NPV,FOR_=FOR_,F_score=F_score,MCC=MCC,BM=BM,MK=MK,TNRv=TNRv,PPVv=PPVv,miss_ratev=miss_ratev,Misclassification_ratev=Misclassification_ratev,FDRv=FDRv,NPVv=NPVv,FOR_v=FOR_v,F_scorev=F_scorev,MCCv=MCCv,BMv=BMv,MKv=MKv)

	f = open(outworkspace + "/report.html","w")
	f.write(html)
	f.close()

