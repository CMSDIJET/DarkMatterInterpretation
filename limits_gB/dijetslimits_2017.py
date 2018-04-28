import ROOT
from fullLims_1cat import getAsymLimits,makeAFillGraph,makeAGraph
from massplot import end,make2DGraph,avtotwidth,parser
import math,sys,time,os,glob,tdrstyle
from array import array
tdrstyle.setTDRStyle()
ROOT.gStyle.SetPadRightMargin(0.065);
ROOT.gStyle.SetPadLeftMargin(0.18);
ROOT.gStyle.SetPadBottomMargin(0.15);
ROOT.gStyle.SetPalette(109);


def DMConstraintsInfty(x):

	mM = x[0];
	return 3/2./6.;

def DMConstraintsM0(x):

	mt = 173.;
	mM = x[0];
	term2 = 0.;
	if mM > 2*mt: term2 = math.sqrt( 1 - 4.*mt*mt/mM/mM );

	nf = 5 + term2;

	num = (9./4.);
	den = 1.+(16./3./nf);

	return math.sqrt(num/den)/6.;

def main():

	# read in the data: 
#	fin2 = ROOT.TFile("limits_freq_gg_qg_qq_pfdijet2016_95CL_moriondDataset_JECV1_35900pb.root")
        #fin2 = ROOT.TFile("limits_freq_qq_pfdijet2017_95CL_Dataset_0p05.root");
 	fin2 = ROOT.TFile("limits_freq_qq_pfdijet2017_95CL_Dataset.root")
#	fin2 = ROOT.TFile("adsfaf.root")

	obshi  = fin2.Get("obs_qq_pfdijet2017");
	exphi1 = fin2.Get("exp1sigma_qq_pfdijet2017");
	exphi2 = fin2.Get("exp2sigma_qq_pfdijet2017");

	#print obshi,exphi1,exphi2
	#print obshi.GetN()

	xs = dijetxs();
	obs_gq = getobs(obshi,xs);
	exp_gq, exp1s_gq = getexp(exphi1,xs);
	exp_gq_tmp2, exp2s_gq = getexp(exphi2,xs);

	exp_gq.SetLineStyle(2);
	exp1s_gq.SetFillStyle(1001);
	exp1s_gq.SetFillColor(ROOT.kGreen+1);
	exp2s_gq.SetFillStyle(1001);
	exp2s_gq.SetFillColor(ROOT.kOrange);

	#--------------------------------
	DMM0func = ROOT.TF1("DMM0func",DMConstraintsM0,0,5000,0);
	DMMInffunc = ROOT.TF1("DMMInffunc",DMConstraintsInfty,0,5000,0);
	DMM0func.SetLineColor(ROOT.kGray+2);
	DMMInffunc.SetLineColor(ROOT.kGray+2);
	DMM0func.SetLineStyle(3);
	DMMInffunc.SetLineStyle(3);
	DMM0func.SetLineWidth(2);
	DMMInffunc.SetLineWidth(2);

	#--------------------------------
	# PLOTTING
	lowlim = 1400;

	txta = ROOT.TLatex(0.22,0.88,"CMS"); txta.SetNDC();
	txtc = ROOT.TLatex(0.63,0.96,"77.8 fb^{-1} (13 TeV)");
	txtc.SetNDC(); txtc.SetTextFont(42); txtc.SetTextSize(0.04);

	txtd = ROOT.TLatex(0.22,0.82,"95% CL upper limits");
	txtd.SetNDC(); txtd.SetTextFont(42); txtd.SetTextSize(0.04);
	
	leg = ROOT.TLegend(0.20,0.61,0.6,0.81);
	leg.SetFillStyle(0);
	leg.SetFillColor(0);    
	leg.SetBorderSize(0);
	leg.SetTextFont(42); 
	# leg.AddEntry(obs_gq,"95% CL upper limits","")
	leg.AddEntry(obs_gq,"Observed","l")
	leg.AddEntry(exp_gq,"Expected","l")
	leg.AddEntry(exp1s_gq,"#pm 1 std. deviation","f")
	leg.AddEntry(exp2s_gq,"#pm 2 std. deviation","f")

	can_gB = ROOT.TCanvas("can_gB","can_gB",900,800);
	hrl = can_gB.DrawFrame(lowlim,0,5101,1.3);
	hrl.GetYaxis().SetTitle("Coupling #font[12]{g#it{_{q}}'}");
	hrl.GetYaxis().SetTitleOffset(1.4);
	hrl.GetXaxis().SetTitle("Z\' mass [GeV]");
	hrl.GetYaxis().SetLabelSize(0.045);
	hrl.GetXaxis().SetLabelSize(0.045);

	txt1 = ROOT.TLatex(0.7,0.28,"m_{DM} > M_{Med} / 2");
	txt1.SetNDC(); txt1.SetTextFont(42); txt1.SetTextSize(0.035);
	txt2 = ROOT.TLatex(0.70,0.23,"m_{DM} = 0");
	txt2.SetNDC(); txt2.SetTextFont(42); txt2.SetTextSize(0.035);

	exp2s_gq.Draw("f");
	exp1s_gq.Draw("fsames");
	obs_gq.Draw("l");
	exp_gq.Draw("l");
	DMM0func.Draw("SAMES")
	DMMInffunc.Draw("SAMES")
	txta.Draw();
	txtc.Draw();
	txtd.Draw();
	txt1.Draw();
	txt2.Draw();
	leg.Draw();

	#line1 = ROOT.TLine(1800,0.02,1800,0.23)
	#line1.SetLineStyle(2)
	#line1.SetLineWidth(2)
	#line1.SetLineColor(ROOT.kGray+1)
	#line1.Draw()
	lab = ROOT.TLatex()
	lab.SetTextSize(0.035)
	lab.SetTextFont(42)
	lab.SetTextColor(ROOT.kGray+1)
	lab.SetTextAlign(33)
	#lab.DrawLatex(1600-10,0.08,"#leftarrow")
	#lab.SetTextAlign(13)
	#lab.DrawLatex(1800+10,0.08,"#rightarrow") 
	#lab.SetTextAlign(23)
	#lab.DrawLatex(1600-200,0.06,"Low")
	#lab.DrawLatex(1600-200,0.04,"mass")
	#lab.DrawLatex(1800+150,0.105,"High")
	#lab.DrawLatex(1800+150,0.06,"mass")

	ROOT.gPad.RedrawAxis();
	can_gB.SaveAs('limplotsHighMass/gB.pdf');

	hrl.GetXaxis().SetMoreLogLabels(True); 
	hrl.GetXaxis().SetNdivisions(10);      
	hrl.GetXaxis().SetNoExponent(True);   
	ROOT.gPad.SetLogx();
	can_gB.SaveAs('limplotsHighMass/gB_logx.pdf');	

def divide(iG,iXS,iGB=False,iGDM=1,iGQ=0.25,iMDM=1.):
	for i0 in range(0,iG.GetN()):
		iG.GetY()[i0] = iG.GetY()[i0]/iXS.Eval(iG.GetX()[i0])/(5./6.)
		lDMWidth = avtotwidth(2,iGDM,iGQ,iG.GetX()[i0],iMDM)
		lWidth   = avtotwidth(2,0.  ,iGQ,iG.GetX()[i0],iMDM)
		iG.GetY()[i0] = (lWidth/lDMWidth)*iG.GetY()[i0]
		if iGB:
			iG.GetY()[i0]=(math.sqrt(iG.GetY()[i0]))*0.25*6

def getobs(obshi,xs):

	x = [];
	y = [];
	iGDM=1;iGQ=0.25;iMDM=1.;

#	for i in range( obslo.GetN() ):

#		lDMWidth = avtotwidth(2,iGDM,iGQ,obslo.GetX()[i],iMDM)
#		lWidth   = avtotwidth(2,0.  ,iGQ,obslo.GetX()[i],iMDM)

#		if obslo.GetX()[i] < 600.0 : continue

#		factor = xs.Eval( obslo.GetX()[i] ) / (6./5.); 

#		x.append( obslo.GetX()[i] );
#		y.append( math.sqrt( (lWidth/lDMWidth)*obslo.GetY()[i] / factor ) / 4. );

	for i in range( obshi.GetN() ):

		lDMWidth = avtotwidth(2,iGDM,iGQ,obshi.GetX()[i],iMDM)
		lWidth   = avtotwidth(2,0.  ,iGQ,obshi.GetX()[i],iMDM)		

		if obshi.GetX()[i] > 6000.: break
		if obshi.GetX()[i] < 1800 : continue

		factor = xs.Eval( obshi.GetX()[i] ) / (6./5.);

		x.append( obshi.GetX()[i] );
		y.append( math.sqrt( (lWidth/lDMWidth)*obshi.GetY()[i] / factor ) / 4. );

	obs_gr = makeAGraph( x, y );
	
	return obs_gr

def getexp(exphi,xs):

	x = [];
	y = [];
	yup = []; 
	ydn = []; 
	iGDM=1;iGQ=0.25;iMDM=1.;

#	for i in range( explo.GetN() ):

#		lDMWidth = avtotwidth(2,iGDM,iGQ,explo.GetX()[i],iMDM)
#		lWidth   = avtotwidth(2,0.  ,iGQ,explo.GetX()[i],iMDM)

#		if explo.GetX()[i] < 600.0 : continue

#		factor = xs.Eval( explo.GetX()[i] ) / (6./5.);
#		cury   = explo.GetY()[i];
#		curyup = explo.GetY()[i] + explo.GetEYhigh()[i];
#		curydn = explo.GetY()[i] - explo.GetEYlow()[i];
#		cury   /= factor;
#		curyup /= factor;
#		curydn /= factor;

#		x.append( explo.GetX()[i] );
#		y.append( math.sqrt((lWidth/lDMWidth)*cury) / 4. );
#		yup.append( math.sqrt((lWidth/lDMWidth)*curyup) / 4. );
#		ydn.append( math.sqrt((lWidth/lDMWidth)*curydn) / 4. );

	for i in range( exphi.GetN() ):

		lDMWidth = avtotwidth(2,iGDM,iGQ,exphi.GetX()[i],iMDM)
		lWidth   = avtotwidth(2,0.  ,iGQ,exphi.GetX()[i],iMDM)

		if exphi.GetX()[i] > 6000.: break;

		if exphi.GetX()[i] < 1800 : continue
		factor = xs.Eval( exphi.GetX()[i] ) / (6./5.);
		cury   = exphi.GetY()[i];
		curyup = exphi.GetY()[i] + exphi.GetEYhigh()[i];
		curydn = exphi.GetY()[i] - exphi.GetEYlow()[i];

		cury   /= factor;
		curyup /= factor;
		curydn /= factor;

		x.append( exphi.GetX()[i] );
		y.append( math.sqrt((lWidth/lDMWidth)*cury) / 4. );
		yup.append( math.sqrt((lWidth/lDMWidth)*curyup) / 4. );
		ydn.append( math.sqrt((lWidth/lDMWidth)*curydn) / 4. );


	exp_gr = makeAGraph( x, y );
	exp_gr_band = makeAFillGraph( x, ydn, yup );

	return exp_gr, exp_gr_band

def QuaInter(F):
  def Func(x):
     z = 0
     mass = [500.0,1000.0,1500.0,2000.0,2500.0,3000.0,3500.0,4000.0]
     for i in range(len(mass)-1):
	if x >= mass[i] and x<= mass[i+1]:
	   slp =  (math.log(F.Eval(mass[i+1]),10)-math.log(F.Eval(mass[i]),10))/(mass[i+1]-mass[i])
	   z = pow(10,slp*(x-mass[i]) + math.log(F.Eval(mass[i]),10))
	if x >= 4000.0:
	   slp = (math.log(F.Eval(4000),10)-math.log(F.Eval(3500),10))/500.0
	   z = pow(10,slp*(x-4000.0) + math.log(F.Eval(4000.0),10))

     return z
#     for i in mass:
#        term = 1.0
#        for j in [y for y in mass if y!=i]:
#           term = (float(x)-float(j))/(float(i)-float(j))*term
#        z=z+term*F.Eval(i)
#     return  z
  return Func

def Do_Inter(Rate):

  Inter = QuaInter(Rate)
  Return_plot = ROOT.TGraph()
  num = -1
  for M in range(500,6000,100):
     num=num+1
     Return_plot.SetPoint(num,M,Inter(M))
  return Return_plot

def dijetxs():

	## these cross-sections are for gq = 0.25
	 x = array('d', [])
	 y = array('d', [])
#	x.append(500)
#        y.append(55.40972)
#        x.append(1000)
#        y.append(4.52414025)
#        x.append(1500)
#        y.append(0.79851609)
#        x.append(1800)
#        y.append(0.33759726)
#        x.append(1850)
#        y.append(0.29324729)
#        x.append(1900)
#        y.append(0.260401474)
#        x.append(1950)
#        y.append(0.227304732)
#        x.append(2000)
#        y.append(0.196553776)
#        x.append(2050)
#        y.append(0.17330184)
#        x.append(2100)
#        y.append(0.153719988)
#        x.append(2150)
#        y.append(0.134315328)
#        x.append(2200)
#        y.append(0.119162975)
#        x.append(2250)
#        y.append(0.105297536)
#        x.append(2300)
#        y.append(0.09604)
#        x.append(2350)
#        y.append(0.084439523)
#        x.append(2400)
#        y.append(0.07578548)
#        x.append(2450)
#        y.append(0.065941288)
#        x.append(2500)
#        y.append(0.058584504)
#        x.append(2550)
#        y.append(0.052458966)
#        x.append(2600)
#        y.append(0.04685148)
#        x.append(2650)
#        y.append(0.0426141574)
#        x.append(2700)
#        y.append(0.0378496797)
#        x.append(2750)
#        y.append(0.0339966198)
#        x.append(2800)
#        y.append(0.0303367425)
#        x.append(3000)
#        y.append(0.0199853544)
#        x.append(3500)
#        y.append(0.0073829504)
#        x.append(4000)
#        y.append(0.00290383786)
#        x.append(4500)
#        y.append(0.00127515024)
#        x.append(5000)
#        y.append(0.0005965878)
#        x.append(5500)
#        y.append(0.000311786336)
#        x.append(6000)
#        y.append(0.000174678885)
#        x.append(6500)
#        y.append(0.000105331028)
#        x.append(7000)
#        y.append(6.7976986e-5)
	 x.append(500)
  	 y.append(59.614102)
         x.append(1000)
         y.append(4.39442892)
         x.append(1500)
         y.append(0.7484672)
         x.append(2000)
         y.append(0.180830)
         x.append(2500)
         y.append(0.0507625)
         x.append(3000)
         y.append(0.015260852)
         x.append(3500)
         y.append(0.004857242)
         x.append(4000)
         y.append(0.001624735)


	 lGraph    = makeAGraph( x, y, 1, 3 )
	 lGraph.SetMarkerColor(1)
	 lGraph = Do_Inter(lGraph)
	 for i in range(500,5500,10):
	   print '\t '+'x.append('+str(i)+')'
	   print '\t '+'y.append('+str(lGraph.Eval(i))+')'
#	   print lGraph.Eval(i), i
	 return lGraph


########################################################################################

def makeAGraph(listx,listy,linecolor = 1, linestyle = 1):

	a_m = array('d', []);
	a_g = array('d', []);

	for i in range(len(listx)):
		a_m.append(listx[i]);
		a_g.append(listy[i]);


	gr = ROOT.TGraph(len(listx),a_m,a_g);

	gr.SetLineColor(linecolor)
	gr.SetLineStyle(linestyle)
	gr.SetLineWidth(2)

	return gr

def makeAFillGraph(listx,listy1,listy2,linecolor = 1, fillcolor = 0, fillstyle = 0):

	a_m = array('d', []);
	a_g = array('d', []);

	for i in range(len(listx)):
		a_m.append(listx[i]);
		a_g.append(listy1[i]);
	
	for i in range(len(listx)-1,-1,-1):
		a_m.append(listx[i]);
		a_g.append(listy2[i]);

	gr = ROOT.TGraph(2*len(listx),a_m,a_g);

	gr.SetLineColor(linecolor)
	gr.SetFillColor(fillcolor)
	gr.SetFillStyle(fillstyle)

	return gr    

if __name__ == '__main__':
	
	main();
