from ROOT import *
import numpy

med = "V"

if med == "V" : f1=TFile.Open("MMedMDM_V.root")
if med == "AV": f1=TFile.Open("MMedMDM_AV.root")

g_obs=f1.Get("obs")

g_clone = g_obs.Clone()

C=TCanvas()

a=numpy.ndarray((1))
a[0]=0.25

h_obs=g_obs.GetHistogram()
h_obs.SetContour(1,a)

g_obs.Draw("col2z")
h_obs.Draw("contz list")
C.Update()

mycontoursarray=gROOT.GetListOfSpecials().FindObject("contours")
print "mycontoursarray = ", mycontoursarray
mylist=mycontoursarray.At(0)
print "mylist = ", mylist

C2=TCanvas("C2","C2")

g_clone.Draw("col2z")

for i in range(0,mylist.GetSize()):
    g_i = mylist.At(i)
    g_i.SetLineWidth(5)
    g_i.SetLineColor(kRed+4)
    g_i.SetLineStyle(kDashed)
    g_i.Draw("lp,same")

if med == "V" : f_obs = TFile("Trijet_V_MM_ICHEP2016_obs.root","RECREATE")
if med == "AV": f_obs = TFile("Trijet_AV_MM_ICHEP2016_obs.root","RECREATE")

mylist.At(0).Write("trijet_obs")


