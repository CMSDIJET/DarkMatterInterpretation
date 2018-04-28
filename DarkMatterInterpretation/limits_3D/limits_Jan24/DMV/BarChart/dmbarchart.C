
#include "TStyle.h"
#include "TCanvas.h"
#include "TFrame.h"
#include "TH1F.h"
#include "TMathText.h"
#include "TLatex.h"
#include "TLegend.h"
#include "TArrow.h"
#include <iostream>


void setSummaryStyle();


void dmbarchart() {

  setSummaryStyle();


  /*****************************/
  /***   Constants section   ***/
  /*****************************/

  // number of enntries in the bar chart
  const Int_t   nAna      = 9;
  const Bool_t  dolog     = true;
  const Float_t minexcl   = 0.5;   // for log
  const Float_t maxexcl   = 10000; // for log
  //const Float_t minexcl = -3;    // for lin
  //const Float_t maxexcl = 2000;  // for lin


  // values for the mediator chart
  Float_t medlowval [nAna] = {    0,   0,   0,   0,   0,   0,   0,   0,   0 };
  Float_t medhighval[nAna] = { 1340,1300, 600, 615,1100,  85, 470,  10,  10 };
  // values for the dm chart
  Float_t dmlowval  [nAna] = {    0,   0,   0,   0,   0,   0,   0,   0,   0 };
  Float_t dmhighval [nAna] = {  440, 310, 210, 150,   0,  36, 175,   1,   1 };

  // labels for the bar chart
  TString label[nAna] = { 
    "#splitline{DM + jets/V(q#bar{q})}{#scale[0.7]{#splitline{#mbox{   }Vector; g_{DM}=g_{q}=1}{#mbox{                                          }}}}",
    "#splitline{DM + jets/V(q#bar{q})}{#scale[0.7]{#splitline{#mbox{   }Axial vector; g_{DM}=g_{q}=1}{#mbox{                                          }}}}",
    "#splitline{DM + #gamma}{#scale[0.7]{#splitline{#mbox{   }Vector; g_{DM}=1, g_{q}=0.25}{#mbox{                                          }}}}",
    "#splitline{DM + #gamma}{#scale[0.7]{#splitline{#mbox{  }Axial vector; g_{DM}=1, g_{q}=0.25}{#mbox{                                          }}}}",
    "#splitline{DM + t}{#scale[0.7]{#splitline{#mbox{   }FC Vector; a_{FC}=b_{FC}=0.1}{#mbox{                                          }}}}",
    "#splitline{DM + jets/V(q#bar{q})}{#scale[0.7]{#splitline{#mbox{   }Scalar; g_{DM}=g_{q}=1}{#mbox{                                          }}}}",
    "#splitline{DM + jets/V(q#bar{q})}{#scale[0.7]{#splitline{#mbox{   }Pseudoscalar; g_{DM}=g_{q}=1}{#mbox{                                          }}}}",
    "#splitline{DM + b#bar{b}/t#bar{t}}{#scale[0.7]{#splitline{#mbox{   }Scalar; g_{DM}=g_{q}=1}{#mbox{                                          }}}}",
    "#splitline{DM + b#bar{b}/t#bar{t}}{#scale[0.7]{#splitline{#mbox{   }Pseudoscalar; g_{DM}=g_{q}=1}{#mbox{                                          }}}}",
  };

  TString pasnr[nAna] = {
    "#splitline{EXO-16-013}{#scale[0.8]{#color[15]{13TeV, 2.3fb^{-1}}}}",
    "#splitline{EXO-16-013}{#scale[0.8]{#color[15]{13TeV, 2.3fb^{-1}}}}",
    "#splitline{EXO-16-014}{#scale[0.8]{#color[15]{13TeV, 2.3fb^{-1}}}}",
    "#splitline{EXO-16-014}{#scale[0.8]{#color[15]{13TeV, 2.3fb^{-1}}}}",
    "#splitline{EXO-16-017}{#scale[0.8]{#color[15]{13TeV, 2.3fb^{-1}}}}",
    "#splitline{EXO-12-055}{#scale[0.8]{#color[15]{8TeV, 19.7fb^{-1}}}}",
    "#splitline{EXO-12-055}{#scale[0.8]{#color[15]{8TeV, 19.7fb^{-1}}}}",
    "#splitline{B2G-15-007}{#scale[0.8]{#color[15]{13TeV, 2.17fb^{-1}}}}",
    "#splitline{B2G-15-007}{#scale[0.8]{#color[15]{13TeV, 2.17fb^{-1}}}}",
  };

  // CL values
  TString conflev[nAna] = {
    "90%CL",
    "90%CL",
    "95%CL",
    "95%CL",
    "95%CL",
    "90%CL",
    "90%CL",
    "95%CL",
    "95%CL",
  };
  

  /***************************/
  /***   Drawing section   ***/
  /***************************/

  // make the canvas
  TCanvas * c = new TCanvas();
  if (dolog) c->SetLogx();

  // histogran declaration
  TH1F * hmedlow  = new TH1F("hmedlow" ,"",nAna,0,nAna);
  TH1F * hmedhigh = new TH1F("hmedhigh","",nAna,0,nAna);
  TH1F * hdmlow   = new TH1F("hdmlow"  ,"",nAna,0,nAna);
  TH1F * hdmhigh  = new TH1F("hdmhigh" ,"",nAna,0,nAna);
  TH1F * hunilow  = new TH1F("hunilow" ,"",nAna,0,nAna);
  TH1F * hunihigh = new TH1F("hunihigh","",nAna,0,nAna);
  TH1F * h = hmedhigh; // base histo, doesn't matter which one

  // fill the histograms
  for (Int_t i = 1; i <= nAna; ++i) {
    Int_t idx = nAna-i; // count backwards
    h->GetXaxis()->SetBinLabel(i, label[idx]);
    if (dmhighval[idx] != 0) {
      hmedhigh ->SetBinContent(i, medhighval[idx]);
      hmedlow  ->SetBinContent(i, medlowval [idx]);
      hdmhigh  ->SetBinContent(i, dmhighval [idx]);
      hdmlow   ->SetBinContent(i, dmlowval  [idx]);
      hunihigh ->SetBinContent(i, 0);
      hunilow  ->SetBinContent(i, 0);
    } else {
      hmedhigh ->SetBinContent(i, 0);
      hmedlow  ->SetBinContent(i, 0);
      hdmhigh  ->SetBinContent(i, 0);
      hdmlow   ->SetBinContent(i, 0);
      hunihigh ->SetBinContent(i, medhighval[idx]);
      hunilow  ->SetBinContent(i, medlowval [idx]);
    }
  }

  // histogram cosmetics
  hmedhigh ->SetBarWidth(0.35); hmedhigh ->SetBarOffset(0.14); hmedhigh ->SetFillColor(kAzure+8);
  hmedlow  ->SetBarWidth(0.35); hmedlow  ->SetBarOffset(0.14); hmedlow  ->SetFillColor(0);       
  hdmhigh  ->SetBarWidth(0.35); hdmhigh  ->SetBarOffset(0.49); hdmhigh  ->SetFillColor(kRed-9);  
  hdmlow   ->SetBarWidth(0.35); hdmlow   ->SetBarOffset(0.49); hdmlow   ->SetFillColor(0);       
  hunihigh ->SetBarWidth(0.35); hunihigh ->SetBarOffset(0.32); hunihigh ->SetFillColor(kAzure+8);
  hunilow  ->SetBarWidth(0.35); hunilow  ->SetBarOffset(0.32); hunilow  ->SetFillColor(0);       

  // prepare the base layer histogram
  h->SetTickLength(0.02);
  h->GetYaxis()->SetTitle("Maximal excluded mass [GeV]");
  h->GetXaxis()->LabelsOption("d");
  h->SetMinimum(minexcl);
  h->SetMaximum(maxexcl);

  // draw the bars
  h       ->Draw("hbar");
  hunihigh->Draw("hbar same");
  hunilow ->Draw("hbar same");
  hmedhigh->Draw("hbar same");
  hmedlow ->Draw("hbar same");
  hdmhigh ->Draw("hbar same");
  hdmlow  ->Draw("hbar same");

  // add the legend for the bars
  TLegend * l = new TLegend(0.01,0.02,0.4,0.07);
  l->SetBorderSize(0);
  l->SetFillStyle(0);
  l->SetNColumns(2);
  l->AddEntry(hmedhigh, "Mediator exclusion", "F");
  l->AddEntry(hdmhigh,  "DM exclusion", "F");
  l->Draw();

  // add PAS label and confidence level
  TLatex lpascl;
  lpascl.SetNDC(kTRUE);
  for (Int_t i = 1; i <= nAna; ++i) {
    lpascl.SetTextSize(0.03);
    lpascl.SetTextColor(1);
    lpascl.DrawLatex(0.89, 0.865-(i-1)*0.765/nAna, pasnr[i-1]);
    lpascl.SetTextSize(0.025);
    lpascl.SetTextColor(15);
    lpascl.DrawLatex(0.83, 0.865-(i-1)*0.765/nAna, conflev[i-1]);
  }

  // add CMS Preliminary and plot title
  TLatex lrm; lrm.SetTextSize(0.04); lrm.SetNDC(kTRUE);
  TLatex lit; lit.SetTextSize(0.04); lit.SetNDC(kTRUE); lit.SetTextFont(72);
  lrm.DrawLatex(0.2, 0.94, "CMS");
  lit.DrawLatex(0.255, 0.94, "Preliminary");
  lrm.SetTextAlign(31);
  lrm.DrawLatex(0.88, 0.94, "Dark Matter Summary* - June 2016");
  lrm.SetTextAlign(11);
  lrm.SetTextColor(17);
  lrm.SetTextSize(0.02);
  lrm.DrawLatex(0.02, 0.1, "*Observed limits");
  lrm.DrawLatex(0.025, 0.08, "Theory uncertainties not included");
  
  // This piece draws the division between spin 0 and spin 1 mediators.
  Int_t divat = 4;  // hardcoded analysis number where to separate
  TArrow * a = new TArrow();
  a->SetLineStyle(2);
  a->SetLineColor(15);
  a->DrawLine(minexcl, divat, maxexcl, divat);
  a->SetLineStyle(9);
  a->SetFillColor(15);
  a->DrawArrow(2500, 0    , 2500, divat, 0.01, "<|>"); // no DrawNDC so it's manual work
  a->DrawArrow(2500, divat, 2500, nAna , 0.01, "<|>"); // no DrawNDC so it's manual work
  TLatex lrot;
  lrot.SetNDC(kTRUE);
  lrot.SetTextSize(0.025);
  lrot.SetTextAngle(270);
  lrot.SetTextColor(15);
  lrot.DrawLatex(0.795, 0.405, "spin 0 mediator");
  lrot.DrawLatex(0.795, 0.785, "spin 1 mediator");

  // hard code extra settings for DM+bbbar
  TLatex ltanb;
  ltanb.SetNDC(kTRUE);
  ltanb.SetTextSize(0.022);
  ltanb.DrawLatex(0.135, 0.200, "#sigma/#sigma_{0} = 30");
  ltanb.DrawLatex(0.135, 0.285, "#sigma/#sigma_{0} = 5");
  

  // redraw axes and grids to make the right things come on top
  h->Draw("AXIG SAME");
  TFrame * fr = c->GetFrame();
  fr->Draw();
  
  // save the canvas
  c->SaveAs("dmbarchart.png");
  c->SaveAs("dmbarchart.pdf");

}


void setSummaryStyle() {
  TStyle * summaryStyle;
  summaryStyle = new TStyle("summaryStyle", "Style for summaries");

  // For the canvas:
  summaryStyle->SetCanvasBorderMode(0);
  summaryStyle->SetCanvasColor(kWhite);
  summaryStyle->SetCanvasDefH(600); //Height of canvas
  summaryStyle->SetCanvasDefW(1000); //Width of canvas
  summaryStyle->SetCanvasDefX(0);   //POsition on screen
  summaryStyle->SetCanvasDefY(0);

  // For the Pad:
  summaryStyle->SetPadBorderMode(0);
  // summaryStyle->SetPadBorderSize(Width_t size = 1);
  summaryStyle->SetPadColor(kWhite);
  summaryStyle->SetPadGridX(kTRUE);
  summaryStyle->SetPadGridY(kFALSE);
  summaryStyle->SetGridColor(0);
  summaryStyle->SetGridStyle(3);
  summaryStyle->SetGridWidth(1);

  // For the frame:
  summaryStyle->SetFrameBorderMode(0);
  summaryStyle->SetFrameBorderSize(1);
  summaryStyle->SetFrameFillColor(0);
  summaryStyle->SetFrameFillStyle(0);
  summaryStyle->SetFrameLineColor(1);
  summaryStyle->SetFrameLineStyle(1);
  summaryStyle->SetFrameLineWidth(1);

  // For the histo:
  // summaryStyle->SetHistFillColor(1);
  // summaryStyle->SetHistFillStyle(0);
  summaryStyle->SetHistLineColor(1);
  summaryStyle->SetHistLineStyle(0);
  summaryStyle->SetHistLineWidth(1);
  summaryStyle->SetMarkerStyle(20);

  // For the statistics box:
  summaryStyle->SetOptFile(0);
  summaryStyle->SetOptStat(0);

  // Margins:
  summaryStyle->SetPadTopMargin(0.08);
  summaryStyle->SetPadBottomMargin(0.15);
  summaryStyle->SetPadLeftMargin(0.2);
  summaryStyle->SetPadRightMargin(0.12);

  // For the Global title:
  summaryStyle->SetOptTitle(0);

  // For the axis titles:
  summaryStyle->SetTitleColor(1, "XYZ");
  summaryStyle->SetTitleFont(42, "XYZ");
  summaryStyle->SetTitleSize(0.055, "XYZ");
  // summaryStyle->SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
  // summaryStyle->SetTitleYSize(Float_t size = 0.02);
  summaryStyle->SetTitleXOffset(0.9);
  summaryStyle->SetTitleYOffset(1.2);
  // summaryStyle->SetTitleOffset(1.1, "Y"); // Another way to set the Offset

  // For the axis labels:
  summaryStyle->SetLabelColor(1, "XYZ");
  summaryStyle->SetLabelFont(42, "XYZ");
  summaryStyle->SetLabelOffset(0.007, "XYZ");
  summaryStyle->SetLabelSize(0.05, "XYZ");
  summaryStyle->SetLabelSize(0.045, "Y"); // SL added

  // For the axis:
  summaryStyle->SetAxisColor(1, "XYZ");
  summaryStyle->SetStripDecimals(kTRUE);
  summaryStyle->SetTickLength(0.03, "XYZ");
  summaryStyle->SetNdivisions(510, "XYZ");
  summaryStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
  summaryStyle->SetPadTickY(1);

  // Change for log plots:
  summaryStyle->SetOptLogx(0);
  summaryStyle->SetOptLogy(0);
  summaryStyle->SetOptLogz(0);

  summaryStyle->cd();

}

