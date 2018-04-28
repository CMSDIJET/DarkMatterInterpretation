from ROOT import *
import sys
#import ast

tgraph= TGraph(sys.argv[1])
#print(sys.argv[1])
#tgraph= TGraph("MetxCombo2016_2/Dijet/ScanMM/Dijet_MM_A_Dijetpaper2016_obs.txt")
tgraph.SetName("Obs_90")
tgraph.SetTitle("Dijet Observed MM 90%CL")
tgraph.SetLineColor(kBlack)
tgraph.GetXaxis().SetTitle("DM mass (GeV)")
tgraph.GetYaxis().SetTitle("#sigma_{SD} (cm^{2})")

f=TFile(sys.argv[2],"recreate")
tgraph.Write()
