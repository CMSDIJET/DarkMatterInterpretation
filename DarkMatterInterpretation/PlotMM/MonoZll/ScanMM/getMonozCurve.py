from ROOT import *
import numpy

med = "V"#V/A/SI/SD

if   med=="V"  : f1=TFile.Open("monoz_exo16038_V.root")
elif med=="AV" : f1=TFile.Open("monoz_exo16038_A.root")

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
    if i==0: g_i.Draw("lp,same")

if   med == "V"  : f_obs = TFile("Monoz_V_MM_ICHEP2016_obs.root","RECREATE")
elif med == "AV" : f_obs = TFile("Monoz_A_MM_ICHEP2016_obs.root","RECREATE")

if   med == "V" or med=="AV": mylist.At(0).Write("monoz_obs")


