########################################
### Example how to plot relic curves ###
########################################

from ROOT import *

f=TFile("./relicContour_A_g25.root")

### list of tgraphs
mylist=f.Get("mytlist")

### loop over (possibly multiple) tgraphs
for i in range(0,mylist.GetSize()):
    if i==0: mylist.At(i).Draw()
    else   : mylist.At(i).Draw("same")
