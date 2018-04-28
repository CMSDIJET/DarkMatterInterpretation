from ROOT import *
import numpy

med = "SD"#V/A/SI/SD

if   med=="V"  : f1=TFile.Open("monophoton_V.root")
elif med=="AV" : f1=TFile.Open("monophoton_AV.root")
elif med=="SI" : f1=TFile.Open("monophoton_SI.root")
elif med=="SD" : f1=TFile.Open("monophoton_SD.root")

g_obs=f1.Get("g_obs")

g_clone = g_obs.Clone()

C=TCanvas()

a=numpy.ndarray((1))
a[0]=1

h_obs=g_obs.GetHistogram()
h_obs.SetContour(1,a)

g_obs.Draw("col2z")
h_obs.Draw("contz list")
C.Update()

mycontoursarray=gROOT.GetListOfSpecials().FindObject("contours")
print "mycontoursarray = ", mycontoursarray
mylist=mycontoursarray.At(0)
print "mylist = ", mylist
print "mylist size = ", mylist.GetSize()

C2=TCanvas("C2","C2")

g_clone.Draw("col2z")

for i in range(0,mylist.GetSize()):
    g_i = mylist.At(i)
    g_i.SetLineWidth(5)
    g_i.SetLineColor(kRed+4)
    g_i.SetLineStyle(kDashed)
    if i==1: g_i.Draw("lp,same")

if   med == "V"  : f_obs = TFile("Monophoton_V_MM_ICHEP2016_obs.root","RECREATE")
elif med == "AV" : f_obs = TFile("Monophoton_A_MM_ICHEP2016_obs.root","RECREATE")
elif med == "SI" : f_obs = TFile("Monophoton_SI_MM_ICHEP2016_obs.root","RECREATE")
elif med == "SD" : f_obs = TFile("Monophoton_SD_MM_ICHEP2016_obs.root","RECREATE")

if   med == "V" or med=="AV": mylist.At(1).Write("monophoton_obs")
elif med == "SI" : mylist.At(1).Write("monophoton_obs")
elif med == "SD" : mylist.At(1).Write("monophoton_obs")


