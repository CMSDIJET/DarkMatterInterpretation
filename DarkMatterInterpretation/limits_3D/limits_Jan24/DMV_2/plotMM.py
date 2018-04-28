#########################################
#########################################
###                                   ###
### Draw awesome MET+X Summary plots  ###
###                                   ###
### (c) MET+X Combo                   ###
###                                   ###
#########################################
#########################################

from ROOT import *
import ast

#################################
### Parameters to be modified ###
#################################

Mediator  = raw_input('Choose mediator [Vector or Axial]: ')
METXonly  = ast.literal_eval(raw_input('MET+X only? [True or False]: '))
DijetOnly = ast.literal_eval(raw_input('Dijet only? [True or False]: '))

#################
### Analyses ####
#################

if Mediator == "Axial": metx = ["monojet","monophoton","monoZ"]
else                  : metx = ["monojet","monophoton","monoZ"]

if Mediator=="Vector" and METXonly : metx+=["monotop"]

if   METXonly  : analyses = ["relic"]+metx
elif DijetOnly : analyses = ["relic","dijet_2016","dijet_2016_exp"]
else           : analyses = ["relic","dijet","trijet"]+metx

tgraph    = {}
color     = {}
text      = {}
filepath  = {}
linestyle = {}

############# 
### Files ###
#############

if Mediator == "Vector":
    filepath["relic"]          = "Relic/relicContour_V_g25.root"
    filepath["dijet"]          = "Dijet/ScanMM/MMedMDM_dijet_v_Phil500.root"
    #ICHEP
    #filepath["dijet_2016"]     = "Dijet/ScanMM/MMedMDM_dijet_v_Phil600.root"
    #filepath["dijet_2016_exp"] = "Dijet/ScanMM/MMedMDM_dijet_v_Phil600.root"
    #paper
    filepath["dijet_2016"]     = "Dijet/ScanMM/Dijet_MM_V_Dijetpaper2016_obs.txt"
    filepath["dijet_2016_exp"] = "Dijet/ScanMM/Dijet_MM_V_Dijetpaper2016_exp.txt"
    filepath["trijet"]         = "Trijet/ScanMM/MMedMDM_v.root"
    filepath["monojet"]        = "Monojet/ScanMM/Monojet_V_MM_ICHEP2016_obs.root"
    filepath["monophoton"]     = "Monophoton/ScanMM/Monophoton_V_MM_ICHEP2016_obs.root"
    #2015: filepath["monoZ"]      = "MonoZll/ScanMM/monoz_vector_gq0p25_cl95_2015.txt"
    filepath["monoZ"]          = "MonoZll/ScanMM/monoz_vector_gq0p25_cl95_2016.txt"
    filepath["monotop"]        = "Monotop/ScanMM/vector_rebinned.root"
elif Mediator == "Axial":
    filepath["relic"]          = "Relic/relicContour_A_g25.root"
    filepath["dijet"]          = "Dijet/ScanMM/MMedMDM_dijet_av_Phil500.root"
    #ICHEP
    #filepath["dijet_2016"]     = "Dijet/ScanMM/MMedMDM_dijet_av_Phil600.root"
    #filepath["dijet_2016_exp"] = "Dijet/ScanMM/MMedMDM_dijet_av_Phil600.root"
    #paper
    filepath["dijet_2016"]     = "Dijet/ScanMM/Dijet_MM_A_Dijetpaper2016_obs.txt"
    filepath["dijet_2016_exp"] = "Dijet/ScanMM/Dijet_MM_A_Dijetpaper2016_exp.txt"
    filepath["trijet"]         = "Trijet/ScanMM/MMedMDM_av.root"
    filepath["monojet"]        = "Monojet/ScanMM/Monojet_AV_MM_ICHEP2016_obs.root"
    filepath["monophoton"]     = "Monophoton/ScanMM/Monophoton_A_MM_ICHEP2016_obs.root"
    #2015: filepath["monoZ"]      = "MonoZll/ScanMM/monoz_axial_gq0p25_cl95_2015.txt"
    filepath["monoZ"]          = "MonoZll/ScanMM/monoz_axial_gq0p25_cl95_2016.txt"

###################
### Plot colors ###
###################

### Planck
linestyle["relic"]          = kDotted
### Met-less
linestyle["dijet"]          = kSolid
linestyle["dijet_2016"]     = kSolid
linestyle["dijet_2016_exp"] = kDashed
linestyle["trijet"]         = kSolid
### MET+X
linestyle["monophoton"]     = kSolid
linestyle["monoZ"]          = kSolid
linestyle["monotop"]        = kDashed
### dummies dashed
linestyle["monojet"]        = kSolid

### Planck
color["relic"]          = kGray
### Met-less
color["dijet"]          = kAzure
color["dijet_2016"]     = kAzure
color["dijet_2016_exp"] = kAzure+1
color["trijet"]         = kAzure+1
color["chi"]            = kBlue
### MET+X
color["monojet"]        = kRed+1#kRed+1
color["monophoton"]     = kOrange+10#kRed+2
color["monoZ"]          = kOrange-3#kRed+3
color["monotop"]        = kViolet+1

##################
### Plot texts ###
##################

if not METXonly:
    text["relic"]          = "\Omega_{c} h^{2} \geq 0.12"
    text["dijet"]          = "#splitline{Dijet #it{[EXO-16-032]}}{+ #it{[arXiv:1604.08907]}}"
    text["dijet_2016"]     = "Observed"
    text["dijet_2016_exp"] = "Expected"
    text["trijet"]         = "#splitline{Boosted dijet}{#it{[EXO-16-030]}}"
    text["chi"]            = "chi obs. (exp.excl.)"
    text["monojet"]        = "#splitline{DM + j/V_{qq}}{#it{[EXO-16-037]}}"
    text["monoZ"]          = "#splitline{DM + Z_{ll}}{#it{[EXO-16-038]}}"
    text["monophoton"]     = "#splitline{DM + #gamma}{#it{[EXO-16-039]}}"
    text["monotop"]        = "#splitline{DM + t (100% FC)}{#it{[EXO-16-040]}}"
else:
    text["relic"]      = "\Omega_{c} h^{2} \geq 0.12"
    text["dijet"]      = "Dijet #it{[EXO-16-032]}+ #it{[arXiv:1604.08907]}"
    text["trijet"]     = "Boosted dijet #it{[EXO-16-030]}}"
    text["chi"]        = "chi obs. (exp.excl.)"
    text["monojet"]    = "DM + j/V_{qq} #it{[EXO-16-037]}"
    text["monoZ"]      = "DM + Z_{ll} #it{[EXO-16-038]}"
    text["monophoton"] = "DM + #gamma #it{[EXO-16-039]}"
    text["monotop"]    = "DM + t (100% FC) #it{[EXO-16-040]}"

####################
### Get graphs   ###
####################

for analysis in analyses: 
    if analysis == "relic":
        mylist = TFile(filepath["relic"]).Get("mytlist")
        print "==> Relic list length = ",mylist.GetSize()
        tgraph["relic"] = mylist.At(0)
    elif analysis == "dijet"          : tgraph["dijet"]          = TFile(filepath[analysis]).Get("obs_025")  
    #ichep
    #elif analysis == "dijet_2016"     : tgraph["dijet_2016"]     = TFile(filepath[analysis]).Get("obs_025")  
    #elif analysis == "dijet_2016_exp" : tgraph["dijet_2016_exp"] = TFile(filepath[analysis]).Get("exp_025")  
    elif analysis == "trijet"         : tgraph["trijet"]         = TFile(filepath[analysis]).Get("obs_025")  
    elif analysis == "monojet"        : tgraph["monojet"]        = TFile(filepath[analysis]).Get("monojet_obs")
    elif analysis == "monophoton"     : tgraph["monophoton"]     = TFile(filepath[analysis]).Get("monophoton_obs")
    #2015: elif analysis == "monoZ"   : tgraph["monoZ"]          = TFile(filepath[analysis]).Get("monoz_obs")
    elif analysis == "monotop"        : tgraph["monotop"]        = TFile(filepath[analysis]).Get("observed")
    else                              : tgraph[analysis]         = TGraph(filepath[analysis])

###################
### Make Canvas ###
### Set ranges  ###
###################

C=TCanvas("C","C",1000,600)
C.cd(1)

C.cd(1).SetTickx()
C.cd(1).SetTicky()

if   METXonly : frame = C.cd(1).DrawFrame(0,0,2000, 780)
else          : frame = C.cd(1).DrawFrame(0,0,3700,1450) 

frame.SetXTitle("M_{Med} [GeV]")
frame.SetYTitle("m_{DM} [GeV]")
#frame.GetXaxis().SetLabelSize(0.05)
#frame.GetYaxis().SetLabelSize(0.05)
frame.GetXaxis().SetTitleSize(0.045)
frame.GetYaxis().SetTitleSize(0.045)
frame.GetXaxis().SetTitleOffset(1.0)
frame.GetYaxis().SetTitleOffset(1.0)

##############
### LEGEND ###
##############

if METXonly:    leg=C.BuildLegend(0.15,0.55,0.45,0.88)
elif DijetOnly: leg=C.BuildLegend(0.70,0.15,0.87,0.36)
else:           leg=C.BuildLegend(0.67,0.12,0.89,0.57)

leg.SetBorderSize(0)
leg.SetTextFont(42)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.Clear()
if DijetOnly: leg.SetHeader("Dijet 95% CL")
else        : leg.SetHeader("#bf{Observed exclusion 90% CL}")

####################
### Add diagonal ###
####################

f1 = TF1("f1","x/2.",0,4000)
g1 = TGraph(f1)
g1.SetLineColor(kGray)
g1.SetLineStyle(kDashed)

if DijetOnly:
    g1.Draw("same")
    legd=TLatex(1300,680,"M_{Med} = 2 x m_{DM}")
    legd.SetTextAngle(38)
    legd.SetTextFont(42)
    legd.SetTextSize(0.025)
    legd.SetTextColor(kGray)
    legd.Draw("same")
elif not METXonly:
    g1.Draw("same")
    legd=TLatex(1600,740,"M_{Med} = 2 x m_{DM}")
    legd.SetTextAngle(45)
    legd.SetTextFont(42)
    legd.SetTextSize(0.025)
    legd.SetTextColor(kGray)
    legd.Draw("same")

##################
### Relic text ###
##################

if Mediator=="Vector" and DijetOnly:
    legw=TLatex(3200,600,"#Omega_{c} h^{2} #geq 0.12")
    legw.SetTextAngle(32)
elif Mediator=="Vector" and not METXonly:
    legw=TLatex(3950,900,"#Omega_{c} h^{2} #geq 0.12")
    legw.SetTextAngle(40)
elif Mediator=="Axial" and DijetOnly:
    legw  = TLatex(1720,1150,"#Omega_{c} h^{2} #geq 0.12")
    legw.SetTextAngle(34)
    legw2 = TLatex(3020,1150,"#Omega_{c} h^{2} #geq 0.12")
    legw2.SetTextFont(42)
    legw2.SetTextColor(color["relic"])
    legw2.SetTextAngle(34)
    legw2.SetTextSize(0.02)
    legw2.Draw("same")
elif Mediator=="Axial" and not METXonly:
    legw  = TLatex(1720,1150,"#Omega_{c} h^{2} #geq 0.12")
    legw.SetTextAngle(40)
    legw2 = TLatex(3020,1150,"#Omega_{c} h^{2} #geq 0.12")
    legw2.SetTextFont(42)
    legw2.SetTextColor(color["relic"])
    legw2.SetTextAngle(40)
    legw2.SetTextSize(0.02)
    legw2.Draw("same")
elif Mediator=="Vector" and METXonly:
    legw=TLatex(1600,160,"#Omega_{c} h^{2} #geq 0.12")
    legw.SetTextAngle(16)
elif Mediator=="Axial" and METXonly:
    legw=TLatex(1750,600,"#Omega_{c} h^{2} #geq 0.12")
    legw.SetTextAngle(35)
legw.SetTextFont(42)
legw.SetTextSize(0.02)
legw.SetTextColor(color["relic"])

##################
### Model text ###
##################

if Mediator=="Vector" and DijetOnly:
    leg1=TLatex(2800,900,"#splitline{#bf{"+Mediator+" mediator}}{#bf{Dirac DM}}")
    leg4=TLatex(2800, 800,"#it{g_{q} = 0.25, g_{DM} = 1}")
    leg4.SetTextFont(42)
    leg4.SetTextSize(0.030)
    leg4.Draw("same")
elif Mediator=="Axial" and DijetOnly:
    leg1=TLatex(2870,800,"#splitline{#bf{"+Mediator+"-vector mediator}}{#bf{Dirac DM}}")
    leg4=TLatex(2870, 700,"#it{g_{q} = 0.25, g_{DM} = 1}")
    leg4.SetTextFont(42)
    leg4.SetTextSize(0.030)
    leg4.Draw("same")
elif Mediator=="Vector" and not METXonly:
    leg1=TLatex(2770,1100,"#splitline{#bf{"+Mediator+" mediator, Dirac DM}}{        #it{g_{q} = 0.25, g_{DM} = 1}}")
elif Mediator=="Axial" and not METXonly:
    leg1=TLatex(3000,1000,"#splitline{#bf{"+Mediator+"-vector mediator, Dirac DM}}{          #it{g_{q} = 0.25, g_{DM} = 1}}")
elif Mediator=="Vector" and METXonly:
    leg1=TLatex(1105,710,"#splitline{#bf{"+Mediator+" mediator, Dirac DM}}{#it{g_{q} = 0.25, g_{DM} = 1}}")
elif Mediator=="Axial" and METXonly:
    leg1=TLatex(1105,705,"#splitline{#bf{"+Mediator+"-vector mediator, Dirac DM}}{#it{g_{q} = 0.25, g_{DM} = 1}}")
leg1.SetTextFont(42)
leg1.SetTextSize(0.030)

################################
### CMS / lumi / energy text ###
################################

if DijetOnly : 
    # CMS
    leg2=TLatex(100,1470,"#bf{CMS}")
    leg2.SetTextFont(42)
    leg2.SetTextSize(0.045)
    # lumi
    leg3=TLatex(2800,1470,"36.4 fb^{-1} (13 TeV)")
    leg3.SetTextFont(42)
    leg3.SetTextSize(0.033)
else         : 
    # CMS
    leg2=TLatex(100,1470,"#bf{CMS} #it{Preliminary}")
    leg2.SetTextFont(42)
    leg2.SetTextSize(0.045)
    # lumi
    leg3=TLatex(2800,1470,"#bf{Dark Matter Summary} #it{ICHEP 2016}")
    leg3.SetTextFont(42)
    leg3.SetTextSize(0.033)

############
### Draw ###
############

for analysis in analyses:
    if not  analysis=="relic":
        leg.AddEntry(tgraph[analysis],text[analysis])

for analysis in analyses:
    tgraph[analysis].SetLineColor(color[analysis])
    tgraph[analysis].SetMarkerSize(0.1)
    tgraph[analysis].SetMarkerColor(color[analysis])
    tgraph[analysis].SetFillColor(color[analysis])
    tgraph[analysis].SetFillStyle(3005)
    tgraph[analysis].SetLineWidth( 202)
    tgraph[analysis].SetLineStyle(linestyle[analysis])
    if analysis == "relic":
        for i in range(0,mylist.GetSize()):
            tgraph["relic"] = mylist.At(i)
            tgraph["relic"].SetLineColor(color[analysis])
            tgraph["relic"].SetFillColor(color[analysis])
            tgraph["relic"].SetLineStyle(linestyle[analysis])
            tgraph["relic"].SetLineWidth(-404)
            tgraph["relic"].SetFillStyle(3005)
            tgraph["relic"].Draw("same")
    elif analysis == "chi":
        tgraph[analysis].SetLineWidth(-404)
    tgraph[analysis].Draw("same")

########################
### Write some texts ###
########################

leg.Draw("same")
leg1.Draw("same")
leg2.Draw("same")
leg3.Draw("same")
legw.Draw("same")

C.Update()

############
### Save ###
############

if METXonly    : C.SaveAs(Mediator+"_METX_Summary_ICHEP.pdf")
elif DijetOnly : C.SaveAs(Mediator+"_Dijet_DM.pdf")
else           : C.SaveAs(Mediator+"_EXO_Summary_ICHEP.pdf")

###########
### FIN ###
###########
