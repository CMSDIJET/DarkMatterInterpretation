import ROOT
from fullLims_1cat import getAsymLimits,makeAFillGraph,makeAGraph
from massplot import end,make2DGraph,avtotwidth,parser
import math,sys,time,os,glob,tdrstyle
from array import array
tdrstyle.setTDRStyle()
ROOT.gStyle.SetPadRightMargin(0.08);
ROOT.gStyle.SetPadLeftMargin(0.14);
ROOT.gStyle.SetPadTopMargin(0.10);
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
	fin = ROOT.TFile("limits_freq_qq_calodijet2016_pfdijet2016.root");

	obslo  = fin.Get("obs_qq_calodijet2016");
	explo1 = fin.Get("exp1sigma_qq_calodijet2016");
	explo2 = fin.Get("exp2sigma_qq_calodijet2016");

	obshi  = fin.Get("obs_qq_pfdijet2016");
	exphi1 = fin.Get("exp1sigma_qq_pfdijet2016");
	exphi2 = fin.Get("exp2sigma_qq_pfdijet2016");

	xs = dijetxs();
	obs_gq = getobs(obslo,obshi,xs);
	exp_gq, exp1s_gq = getexp(explo1,exphi1,xs);
	exp_gq_tmp2, exp2s_gq = getexp(explo2,exphi2,xs);

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
	lowlim = 350;

	txta = ROOT.TLatex(0.16,0.92,"CMS"); txta.SetNDC();
	txtc = ROOT.TLatex(0.73,0.92,"12.9 fb^{-1} (13 TeV)");
	txtc.SetNDC(); txtc.SetTextFont(42); txtc.SetTextSize(0.04);

	txtd = ROOT.TLatex(0.22,0.83,"95% CL upper limits");
	txtd.SetNDC(); txtd.SetTextFont(42); txtd.SetTextSize(0.04);
	
	leg = ROOT.TLegend(0.20,0.63,0.6,0.81);
	leg.SetFillStyle(0);
	leg.SetFillColor(0);    
	leg.SetBorderSize(0);
	leg.SetTextFont(42); 
	# leg.AddEntry(obs_gq,"95% CL upper limits","")
	leg.AddEntry(obs_gq,"Observed","l")
	leg.AddEntry(exp_gq,"Expected","l")
	leg.AddEntry(exp1s_gq,"#pm 1 std. deviation","f")
	leg.AddEntry(exp2s_gq,"#pm 2 std. deviation","f")

	can_gB = ROOT.TCanvas("can_gB","can_gB",1200,800);
	hrl = can_gB.DrawFrame(lowlim,0,4001,0.45);
	hrl.GetYaxis().SetTitle("Coupling g_{q}'");
	hrl.GetYaxis().SetTitleOffset(1.0);
	hrl.GetXaxis().SetTitle("Z\' mass (GeV)");

	txt1 = ROOT.TLatex(0.18,0.58,"m_{DM} > M_{Med} / 2");
	txt1.SetNDC(); txt1.SetTextFont(42); txt1.SetTextSize(0.03);
	txt2 = ROOT.TLatex(0.18,0.46,"m_{DM} = 0");
	txt2.SetNDC(); txt2.SetTextFont(42); txt2.SetTextSize(0.03);

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

def getobs(obslo,obshi,xs):

	x = [];
	y = [];
	iGDM=1;iGQ=0.25;iMDM=1.;

	for i in range( obslo.GetN() ):

		lDMWidth = avtotwidth(2,iGDM,iGQ,obslo.GetX()[i],iMDM)
		lWidth   = avtotwidth(2,0.  ,iGQ,obslo.GetX()[i],iMDM)

		factor = xs.Eval( obslo.GetX()[i] ) / (6./5.); 

		x.append( obslo.GetX()[i] );
		y.append( math.sqrt( (lWidth/lDMWidth)*obslo.GetY()[i] / factor ) / 4. );

	for i in range( obshi.GetN() ):

		lDMWidth = avtotwidth(2,iGDM,iGQ,obshi.GetX()[i],iMDM)
		lWidth   = avtotwidth(2,0.  ,iGQ,obshi.GetX()[i],iMDM)		

		if obshi.GetX()[i] > 3700.: break;

		factor = xs.Eval( obshi.GetX()[i] ) / (6./5.);

		x.append( obshi.GetX()[i] );
		y.append( math.sqrt( (lWidth/lDMWidth)*obshi.GetY()[i] / factor ) / 4. );

	obs_gr = makeAGraph( x, y );
	
	return obs_gr

def getexp(explo,exphi,xs):

	x = [];
	y = [];
	yup = []; 
	ydn = []; 
	iGDM=1;iGQ=0.25;iMDM=1.;

	for i in range( explo.GetN() ):

		lDMWidth = avtotwidth(2,iGDM,iGQ,explo.GetX()[i],iMDM)
		lWidth   = avtotwidth(2,0.  ,iGQ,explo.GetX()[i],iMDM)

		factor = xs.Eval( explo.GetX()[i] ) / (6./5.);
		cury   = explo.GetY()[i];
		curyup = explo.GetY()[i] + explo.GetEYhigh()[i];
		curydn = explo.GetY()[i] - explo.GetEYlow()[i];
		cury   /= factor;
		curyup /= factor;
		curydn /= factor;

		x.append( explo.GetX()[i] );
		y.append( math.sqrt((lWidth/lDMWidth)*cury) / 4. );
		yup.append( math.sqrt((lWidth/lDMWidth)*curyup) / 4. );
		ydn.append( math.sqrt((lWidth/lDMWidth)*curydn) / 4. );

	for i in range( exphi.GetN() ):

		lDMWidth = avtotwidth(2,iGDM,iGQ,exphi.GetX()[i],iMDM)
		lWidth   = avtotwidth(2,0.  ,iGQ,exphi.GetX()[i],iMDM)

		if exphi.GetX()[i] > 3700.: break;

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


def dijetxs():

	## these cross-sections are for gq = 0.25
	x = array('d', [])
	y = array('d', [])
	x.append(500)
	y.append(54.39976667)
	x.append(1000)
        y.append(3.79482905)
	x.append(1500)
        y.append(0.64184835)
	x.append(1800)
        y.append(0.256497348)
	x.append(1900)
        y.append(0.197961717)
	x.append(2000)
        y.append(0.15153154)
	x.append(2100)
        y.append(0.115242345)
	x.append(2200)
        y.append(0.090241305)
	x.append(2300)
        y.append(0.06822651)
	x.append(2400)
        y.append(0.05406678)
	x.append(2500)
        y.append(0.041757683)
	x.append(2600)
        y.append(0.033034138)
	x.append(2700)
        y.append(0.025036183)
	x.append(2800)
        y.append(0.020569049)
	x.append(3000)
        y.append(0.012877625)
	x.append(3500)
        y.append(0.004038073)
	x.append(4000)
        y.append(0.001372723)
	lGraph    = makeAGraph( x, y, 1, 3 )
	lGraph.SetMarkerColor(1)
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
