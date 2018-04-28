##################################
##                               ##
## Visualizing relic constraints ##
## estimated with MadDM          ##
## to our DM models              ##
## on our monojet searches       ##
##                               ##
###################################

### input
 
model=['S','P','V','A']
coupling=[25,33,1,3,4]
region = ['full','PAS','low']

model = raw_input('Choose mediator[S or P or V or A]: ')
coupling = raw_input('Enter the coupling value[25,33,1,3,4]: ')
region = raw_input('Choose range[low or PAS or full]: ')

relicVal=0.12

### imports

import ROOT
from ROOT import *
import numpy
#import filestringmap

########################
### Get MadDM output ###
########################

#filestringmap = {}
#filestringmap['S',1] = "outputMadDM_Scg1_vlb.dat"
#filestringmap['P',1] = "outputMadDM_PS_g1.dat"
#filestringmap['V',1] = "outputMadDM_ZpA.dat"
#filestringmap['A',4,range]

g = TGraph2D("outputMadDM_"+model+"_g"+coupling+"_"+region+".dat")
g.SetNpx(500)
g.SetNpy(500)
#g.SetTitle("#Omega_{c}[m_{Med},m_{DM}] - relic density with MadDM")
#g.SetTitle("MadDM relic density")
g.SetTitle("#Omega_{c} x h^{2}")
g1=g.Clone()
g2=g.Clone()

################
### Diagonal ###
################

d=TLine(3.5,1.750,15000,7500)

##############
### Canvas ###
##############

#C=TCanvas("C","C",1000,500)
#C.Divide(2)
#C.cd(1)

C=TCanvas("C","C",500,500)
C.Divide(1)
C.cd(1)

######################################
### Getting the iso-Omega contour  ###
### Omega=0.12 is relic observable ###
######################################

a=numpy.ndarray((1))
a[0]=relicVal

h=g.GetHistogram()
h.SetContour(1,a)


from ROOT import *
import numpy
from array import array

def set_plot_Style(): 
    NRGBs = 5
    NCont = 255
    stops = [ 0.00, 0.34, 0.51, 0.64, 1.00 ]
    red   = [ 0.00, 0.00, 0.87, 1.00, 0.51 ]
    green = [ 0.00, 0.81, 1.00, 0.20, 0.00 ]
    blue  = [ 0.51, 1.00, 0.12, 0.00, 0.00 ]
    stopsArray = array('d', stops)
    redArray   = array('d', red)
    greenArray = array('d', green)
    blueArray  = array('d', blue)
    TColor.CreateGradientColorTable(NRGBs, stopsArray, redArray, greenArray, blueArray, NCont)
    gStyle.SetNumberContours(NCont)

def scale_graph(g_tmp,g_scale_tmp):
    n=g_tmp.GetN()
    for i in range(0,n):
        x=ROOT.Double()
        y=ROOT.Double()
        g_tmp.GetPoint(i,x,y)
        g_scale_tmp.SetPoint(i,x/1000.,y/1000.)


set_plot_Style()
#g.Draw("col2z")
#h.Draw("contz list")
g_scale=g
h_scale=h
g.Draw("col2z")
h.Draw("contz list")
C.Update()

mycontoursarray=gROOT.GetListOfSpecials().FindObject("contours")
print "mycontoursarray = ", mycontoursarray
mytlist=mycontoursarray.At(0)
print "mytlist = ", mytlist
mytgraphs1=mytlist
mytgraphs2=mytlist.Clone("xxx")
mytgraphs3=mytlist.Clone("yyy")

f=TFile("relicContour_"+model+"_g"+coupling+".root","recreate")
mytlist.Write("mytlist",TObject.kSingleKey)
f.Close()


print "Number of contours = ", mytgraphs1.GetSize()

######################
### Drawing linear ###
######################

g1_scale=g1
#scale_graph(g1,g1_scale)

g1_scale.SetMaximum(1.)
g1_scale.SetMinimum(0.00001)
g1_scale.Draw("col2z")
for graph_entry in range(0,mytgraphs1.GetSize()):
    mytgraph1=mytgraphs1.At(graph_entry)
    mytgraph1_scale=mytgraph1
    #scale_graph(mytgraph1,mytgraph1_scale)

    mytgraph1_scale.SetLineStyle(1)
    mytgraph1_scale.SetLineWidth(5)
    mytgraph1_scale.SetLineColor(kMagenta-4)#kRed+4)
    mytgraph1_scale.Draw("lp,same")

d.SetLineStyle(kDotted)
d.SetLineColor(kWhite)
d.SetLineWidth(3)
d.Draw("lp,same")

g1_scale.GetXaxis().SetTitle("m_{Med} [GeV]")
g1_scale.GetYaxis().SetTitle("m_{DM} [GeV]")
g1_scale.GetYaxis().SetTitleOffset(1.2)
C.Update()

latex1 = TLatex()
latex2 = TLatex()
latex3 = TLatex()

xmin=g1_scale.GetXaxis().GetXmin()
xmax=g1_scale.GetXaxis().GetXmax()
ymin=g1_scale.GetYaxis().GetXmin()
ymax=g1_scale.GetYaxis().GetXmax()

modelName={}
modelName['S']='Scalar'
modelName['P']='Pseudo'
modelName['V']='Vector'
modelName['A']='Axial'

latex1.SetTextColor(kMagenta-4)
latex2.SetTextColor(kMagenta+1)
latex3.SetTextColor(kMagenta+1)

latex1.DrawLatex(xmin+0.005*(xmax-xmin),ymin+0.92*(ymax-ymin),"#Omega_{c} #times h^{2}="+str(relicVal))
latex2.DrawLatex(xmin+0.005*(xmax-xmin),ymin+0.85*(ymax-ymin),modelName[model]) #lower limit
couplingStr = coupling
if   coupling == "25": couplingStr="0.25"
elif coupling == "33": couplingStr="0.33"
latex3.DrawLatex(xmin+0.005*(xmax-xmin),ymin+0.78*(ymax-ymin),"g_{q}="+couplingStr)



C.Update()

C.SaveAs(model+"_g"+str(coupling)+"_fullrange.png")

bla

###################
### Drawing log ###
###################

C.cd(2).SetLogz()
C.cd(2).SetLogx()
g2.SetMaximum(10.)
g2.SetMinimum(0.00001)
g2.Draw("col2z")

latex1.Draw()
latex2.Draw()
latex3.Draw()

for graph_entry in range(0,mytgraphs2.GetSize()):
    mytgraph2=mytgraphs2.At(graph_entry)
    mytgraph2.SetLineStyle(0)
    mytgraph2.SetLineWidth(5)
    mytgraph2.SetLineColor(kBlue+1)
    mytgraph2.Draw("lp,same")

g2.GetXaxis().SetTitle("m_{Med} [GeV]")
g2.GetYaxis().SetTitle("m_{DM} [GeV]")
g2.GetYaxis().SetTitleOffset(1.2)
C.Update()


latex1 = TLatex()
latex2 = TLatex()
latex3 = TLatex()

#xmin=g1.GetXaxis().GetXmin()
#xmax=g1.GetXaxis().GetXmax()
#ymin=g1.GetYaxis().GetXmin()
#ymax=g1.GetYaxis().GetXmax()

latex1.SetTextColor(kBlue+1)
latex2.SetTextColor(kBlue-4)
latex3.SetTextColor(kBlue-4)

latex1.DrawLatex(xmin+0.005*(xmax-xmin),ymin+0.92*(ymax-ymin),"#Omega_{c} #times h^{2}="+str(relicVal))
latex2.DrawLatex(xmin+0.005*(xmax-xmin),ymin+0.85*(ymax-ymin),modelName[model]) #lower limit
couplingStr = coupling
if   coupling == "25": couplingStr="0.25"
elif coupling == "33": couplingStr="0.33"
latex3.DrawLatex(xmin+0.005*(xmax-xmin),ymin+0.78*(ymax-ymin),"g_{qq}="+couplingStr)


#l = TLegend(0.1,0.7,0.48,0.9)
#l.SetHeader("Model","ap")
#l.AddEntry(mytgraph1,"Scalar","ap")
#l.AddEntry(mytgraph1,"g=1","ap")
#l.Draw()


#latex2 = TText()
#latex.DrawText(1310,18480,"Pseudo") upper limit
#latex.DrawText(1310,17300,"g=1")
#latex.DrawText(60,350,"Pseudo") #lower limit
#latex.DrawText(60,320,"g=1")
#latex.DrawText(60,290,"#Omega h^{2}=0.12")



#latex2.DrawText(xmin+0.1*(xmax-xmin),ymin+0.9*(ymax-ymin),model) #lower limit
#latex2.DrawText(xmin+0.1*(xmax-xmin),ymin+0.8*(ymax-ymin),"g="+coupling)
#latex2.DrawText(xmin+0.1*(xmax-xmin),ymin+0.7*(ymax-ymin),"#Omega #times h^{2}=0.12")
C.Update()
C.cd(1)

#latex.DrawText(1310.,18348.,"Pseudo")
#latex.DrawText(1310.,17230.,"g=1")
#latex.DrawText(80,350,"Pseudo")
#latex.DrawText(80,320,"g=1")



f=TFile("mygraph2D.root","recreate")
#mytgraphs3.SetLineWidth(5)
#mytgraphs3.SetLineColor(kMagenta)
#mytgraphs3.SetLineStyle(0)
mytgraphs3.Write()
f.Close()

print "there is a file mytgraph2D waiting for you"
