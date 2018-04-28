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
METXonly  = False #ast.literal_eval(raw_input('MET+X only? [True or False]: '))
DijetOnly = True #ast.literal_eval(raw_input('Dijet only? [True or False]: '))
Dilepton  = False #ast.literal_eval(raw_input('Dilepton? [True or False]: '))
if Dilepton: gl = ast.literal_eval(raw_input('gl? [0.10 or 0.025 or 0.01]: '))

logx      = False #ast.literal_eval(raw_input('Log x? '))

CL = "95"

#################
### Analyses ####
#################

if Mediator == "Axial": metx = ["monojet","monophoton","monoZ"]
else                  : metx = ["monojet","monophoton","monoZ"]

if Mediator=="Vector" and METXonly : metx+=["monotop"]

if   METXonly  : analyses = ["relic"]+metx
elif Dilepton  : analyses = ["relic","dilepton","dijet","trijet"]+metx
elif DijetOnly : analyses = ["relic","dijet_2016","dijet_2016_exp"]
else           : analyses = ["relic","dijet_2016","trijet"]+metx

tgraph    = {}
color     = {}
text      = {}
filepath  = {}
linestyle = {}

############# 
### Files ###
#############

if Mediator == "Vector":
    filepath["relic"]          = "Relic/madDMv2_0_6/relicContour_V_g25.root"
    #ICHEP
    filepath["dijet"]          = "Dijet/ScanMM/MMedMDM_dijet_v_Phil500.root"
    #filepath["dilepton"]       = "Dilepton/ScanMM/MMedMDM_diel_v.root"
    if Dilepton:
        if   gl==0.10  : filepath["dilepton"] = "Dilepton/ScanMM/MMedMDM_diel_v_gl0p10.root"
        elif gl==0.025 : filepath["dilepton"] = "Dilepton/ScanMM/MMedMDM_diel_v_gl0p025.root"
        elif gl==0.01  : filepath["dilepton"] = "Dilepton/ScanMM/MMedMDM_diel_v_gl0p01.root"
    #Dijet paper
    #filepath["dijet_2016"]     = "Dijet/ScanMM/MMedMDM_dijet_v_Phil600.root"
    #filepath["dijet_2016_exp"] = "Dijet/ScanMM/MMedMDM_dijet_v_Phil600.root"
    #95
    if CL=="95":
        filepath["dijet_2016"]     = "Dijet/ScanMM/Dijet_MM_V_Dijetpaper2016_obs_narrow.txt"
        filepath["dijet_2016_exp"] = "Dijet/ScanMM/Dijet_MM_V_Dijetpaper2016_exp_narrow.txt"
    elif CL=="90":
        filepath["dijet_2016"]     = "Dijet/ScanMM/MMedMDM_dijet_v_90_top56.root"
        filepath["dijet_2016_exp"] = "Dijet/ScanMM/MMedMDM_dijet_v_90_top56.root"
    #
    #filepath["dijet_2016"]     = "Dijet/ScanMM/Dijet_MM_V_Dijetpaper2016_obs.txt"
    #filepath["dijet_2016_exp"] = "Dijet/ScanMM/Dijet_MM_V_Dijetpaper2016_exp.txt"
    filepath["trijet"]         = "Trijet/ScanMM/MMedMDM_v.root"
    filepath["monojet"]        = "Monojet/ScanMM/Monojet_V_MM_ICHEP2016_obs.root"
    filepath["monophoton"]     = "Monophoton/ScanMM/Monophoton_V_MM_ICHEP2016_obs.root"
    #2015: filepath["monoZ"]      = "MonoZll/ScanMM/monoz_vector_gq0p25_cl95_2015.txt"
    filepath["monoZ"]          = "MonoZll/ScanMM/monoz_vector_gq0p25_cl95_2016.txt"
    filepath["monotop"]        = "Monotop/ScanMM/vector_rebinned.root"
elif Mediator == "Axial":
    filepath["relic"]          = "Relic/madDMv2_0_6/relicContour_A_g25.root"
    #ICHEP
    filepath["dijet"]          = "Dijet/ScanMM/MMedMDM_dijet_av_Phil500.root"
    #Dijet paper
    #filepath["dijet_2016"]     = "Dijet/ScanMM/MMedMDM_dijet_av_Phil600.root"
    #filepath["dijet_2016_exp"] = "Dijet/ScanMM/MMedMDM_dijet_av_Phil600.root"
    #95
    if CL=="95":
        filepath["dijet_2016"]     = "Dijet/ScanMM/Dijet_MM_A_Dijetpaper2016_obs_narrow.txt"
        filepath["dijet_2016_exp"] = "Dijet/ScanMM/Dijet_MM_A_Dijetpaper2016_exp_narrow.txt"
    elif CL=="90":
        filepath["dijet_2016"]     = "Dijet/ScanMM/MMedMDM_dijet_av_90_top56.root"
        filepath["dijet_2016_exp"] = "Dijet/ScanMM/MMedMDM_dijet_av_90_top56.root"
    #Dijet paper?
    #filepath["dijet_2016"]     = "Dijet/ScanMM/Dijet_MM_A_Dijetpaper2016_obs.txt"
    #filepath["dijet_2016_exp"] = "Dijet/ScanMM/Dijet_MM_A_Dijetpaper2016_exp.txt"
    filepath["trijet"]         = "Trijet/ScanMM/MMedMDM_av.root"
    filepath["monojet"]        = "Monojet/ScanMM/Monojet_AV_MM_ICHEP2016_obs.root"
    filepath["monophoton"]     = "Monophoton/ScanMM/Monophoton_A_MM_ICHEP2016_obs.root"
    #2015: filepath["monoZ"]      = "MonoZll/ScanMM/monoz_axial_gq0p25_cl95_2015.txt"
    filepath["monoZ"]          = "MonoZll/ScanMM/monoz_axial_gq0p25_cl95_2016.txt"

###################
### Plot colors ###
###################

### Planck
linestyle["relic"]          = kDotted#was dotted
### Met-less
linestyle["dijet"]          = kSolid
linestyle["dijet_2016"]     = kSolid
linestyle["dijet_2016_exp"] = kDashed
linestyle["dilepton"]       = kSolid
linestyle["trijet"]         = kSolid
### MET+X
linestyle["monophoton"]     = kSolid
linestyle["monoZ"]          = kSolid
linestyle["monotop"]        = kDashed
### dummies dashed
linestyle["monojet"]        = kSolid

### Planck
color["relic"]          = kGray+2
### Met-less
color["dijet"]          = kAzure
color["dilepton"]       = kGreen+3
color["dijet_2016"]     = kAzure
color["dijet_2016_exp"] = kAzure+1
color["trijet"]         = kAzure+1
color["chi"]            = kBlue
### MET+X
color["monojet"]        = kRed+1#kRed+1
color["monophoton"]     = kGreen+3#kRed+2
color["monoZ"]          = kOrange-3#kRed+3
color["monotop"]        = kViolet+1

##################
### Plot texts ###
##################

if not METXonly:
    text["relic"]          = "\Omega_{c} h^{2} \geq 0.12"
    text["dijet"]          = "#splitline{Z' #rightarrow jj #it{[EXO-16-032]}}{+ #it{[arXiv:1604.08907]}}"
    text["dilepton"]       = "#splitline{Z' #rightarrow e^{+}e^{-}}{#it{[EXO-16-031]}}"
    text["dijet_2016"]     = "#splitline{Dijet}{[EXO-16-056]}"
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
    text["monojet"]    = "#splitline{#scale[0.5]{DM + j/V_{qq}}}{#scale[0.2]{#it{[EXO-16-037]}}}"
    text["monoZ"]      = "#splitline{#scale[0.5]{DM + Z_{ll}}}{#scale[0.2]{#it{[EXO-16-038]}}}"
    text["monophoton"] = "#splitline{#scale[0.5]{DM + #gamma}}{#scale[0.2]{#it{[EXO-16-039]}}}"
    text["monotop"]    = "#splitline{#scale[0.5]{DM + t}}{#scale[0.2]{#it{[EXO-16-040]}}}"

####################
### Get graphs   ###
####################

for analysis in analyses: 
    if analysis == "relic":
        mylist = TFile(filepath["relic"]).Get("mytlist")
        print "==> Relic list length = ",mylist.GetSize()
        tgraph["relic"] = mylist.At(0)
    #ichep
    elif analysis == "dijet"          : tgraph["dijet"]          = TFile(filepath[analysis]).Get("obs_025")  
    #dijet paper
    elif analysis == "dijet_2016"     : tgraph["dijet_2016"]     = TGraph(filepath[analysis])  
    elif analysis == "dijet_2016_exp" : tgraph["dijet_2016_exp"] = TGraph(filepath[analysis])  
    elif analysis == "trijet"         : tgraph["trijet"]         = TFile(filepath[analysis]).Get("obs_025")  
    #
    elif analysis == "dilepton"       : tgraph["dilepton"]       = TFile(filepath[analysis]).Get("obs_025")  
    elif analysis == "monojet"        : tgraph["monojet"]        = TFile(filepath[analysis]).Get("monojet_obs")
    elif analysis == "monophoton"     : tgraph["monophoton"]     = TFile(filepath[analysis]).Get("monophoton_obs")
    #2015: elif analysis == "monoZ"   : tgraph["monoZ"]          = TFile(filepath[analysis]).Get("monoz_obs")
    elif analysis == "monotop"        : tgraph["monotop"]        = TFile(filepath[analysis]).Get("observed")
    else                              : tgraph[analysis]         = TGraph(filepath[analysis])

tgraph["monotop"]        = TFile(filepath[analysis]).Get("observed")
###################
### Make Canvas ###
### Set ranges  ###
###################

C=TCanvas("C","C",1000,600)
C.cd(1)

C.cd(1).SetTickx()
C.cd(1).SetTicky()

if logx       : frame = C.cd(1).DrawFrame(1500,0,5500, 2300)
elif METXonly : frame = C.cd(1).DrawFrame(0,0,2000, 780)
elif Dilepton : frame = C.cd(1).DrawFrame(0,0,5000,2000)
else          : frame = C.cd(1).DrawFrame(1300,0,5500,2300) 

if logx : C.cd(1).SetLogx()

frame.SetXTitle("Mediator mass [GeV]")
frame.SetYTitle("m_{DM} [GeV]")
#frame.GetXaxis().SetLabelSize(0.05)
#frame.GetYaxis().SetLabelSize(0.05)
frame.GetXaxis().SetTitleSize(0.052)#was 45
frame.GetYaxis().SetTitleSize(0.052)#was 45
frame.GetXaxis().SetTitleOffset(0.85)
frame.GetYaxis().SetTitleOffset(0.85)

##############
### LEGEND ###
##############

if   logx     : leg=C.BuildLegend(0.31,0.25,0.51,0.75)
elif METXonly : leg=C.BuildLegend(0.15,0.55,0.45,0.88)
elif Dilepton : leg=C.BuildLegend(0.68,0.12,0.87,0.45)
elif DijetOnly: leg=C.BuildLegend(0.70,0.12,0.86,0.51)
else:           leg=C.BuildLegend(0.67,0.12,0.86,0.51)

leg.SetBorderSize(0)
leg.SetTextFont(42)
leg.SetFillColor(0)
leg.SetFillStyle(0)
leg.Clear()
#if DijetOnly: leg.SetHeader("Dijet "+CL+"% CL")
#else        : leg.SetHeader("#bf{CMS "+CL+"% CL}")



####################
### Add diagonal ###
####################

f1 = TF1("f1","x/2.",0,5000)
g1 = TGraph(f1)
g1.SetLineColor(color["relic"]-1)
g1.SetLineStyle(kDashed)

if Dilepton:
    g1.Draw("same")
    legd=TLatex(1300,680,"M_{Med} = 2 x m_{DM}")
    legd.SetTextAngle(35)
    legd.SetTextFont(42)
    legd.SetTextSize(0.030)
    legd.SetTextColor(color["relic"])
    legd.Draw("same")
elif DijetOnly:
    g1.Draw("same")
    legd=TLatex(2000,860,"M_{Med} = 2 x m_{DM}")
    legd.SetTextAngle(30)
    legd.SetTextFont(42)
    legd.SetTextSize(0.040)
    legd.SetTextColor(color["relic"])
    legd.Draw("same")
elif not METXonly:
    g1.Draw("same")
    legd=TLatex(1600,850,"M_{Med} = 2 x m_{DM}")
    legd.SetTextAngle(41)
    legd.SetTextFont(42)
    legd.SetTextSize(0.040)
    legd.SetTextColor(color["relic"])
    legd.Draw("same")

##################
### Relic text ###
##################

if Mediator=="Vector" and Dilepton:
    legw=TLatex(2700,450,"#Omega_{c} h^{2} #geq 0.12")
    legw.SetTextAngle(20)
    legw.SetTextSize(0.020)
elif Mediator=="Vector" and DijetOnly:
    legw=TLatex(2000,170,"#Omega_{c} h^{2} #geq 0.12")
    legw.SetTextAngle(15)
    legw.SetTextSize(0.04)
elif Mediator=="Vector" and not METXonly:
    legw=TLatex(2750,650,"#Omega_{c} h^{2} #geq 0.12")
    legw.SetTextAngle(35)
    legw.SetTextSize(0.03)
elif Mediator=="Axial" and DijetOnly:
    legw  = TLatex(1670,1070,"#Omega_{c} h^{2} #geq 0.12")
    legw.SetTextAngle(25)
    legw2 = TLatex(1800,580,"#Omega_{c} h^{2} #geq 0.12")
    legw2.SetTextFont(42)
    legw2.SetTextColor(color["relic"])
    legw2.SetTextAngle(25)
    legw.SetTextSize(0.04)
    legw2.SetTextSize(0.04)
    legw2.Draw("same")
elif Mediator=="Axial" and not METXonly:
    legw  = TLatex(1720,1090,"#Omega_{c} h^{2} #geq 0.12")
    legw.SetTextAngle(40)
    legw2 = TLatex(2000,850,"#Omega_{c} h^{2} #geq 0.12")
    legw2.SetTextFont(42)
    legw2.SetTextColor(color["relic"])
    legw2.SetTextAngle(40)
    legw2.Draw("same")
    legw.SetTextSize(0.03)
    legw2.SetTextSize(0.03)
elif Mediator=="Vector" and METXonly:
    legw=TLatex(1600,160,"#Omega_{c} h^{2} #geq 0.12")
    legw.SetTextAngle(16)
    legw.SetTextSize(0.03)
elif Mediator=="Axial" and METXonly:
    legw=TLatex(1750,600,"#Omega_{c} h^{2} #geq 0.12")
    legw.SetTextSize(0.03)
    legw.SetTextAngle(35)
legw.SetTextFont(42)
legw.SetTextColor(color["relic"])

##################
### Model text ###
##################

if logx:
    leg1=TLatex(250,1300,"#splitline{#bf{"+Mediator+" mediator}}{#bf{Dirac DM}}")
    leg1.SetTextFont(42)
    leg1.SetTextSize(0.030)
    leg4=TLatex(250,1200,"#it{g_{q} = 0.25, g_{DM} = 1}")
    leg4.SetTextFont(42)
    leg4.SetTextSize(0.030)
    leg4.Draw("same")
elif Mediator=="Vector" and Dilepton:
    leg1=TLatex(2650,1550,"#splitline{#bf{Vector mediator}}{#bf{Dirac DM}}")
    leg4=TLatex(2650,1350,"#splitline{#it{g_{DM} = 1.0}}{#it{g_{q} = 0.25, g_{l} = "+str(gl)+"}}")
    leg1.SetTextFont(42)
    leg4.SetTextFont(42)
    #leg5.SetTextFont(42)
    leg1.SetTextSize(0.030)
    leg4.SetTextSize(0.030)
    #leg5.SetTextSize(0.030)
    leg4.Draw("same")
    #leg5.Draw("same")
elif Mediator=="Vector" and DijetOnly:
    leg1=TLatex(4500,1080,"Vector mediator")
    leg5=TLatex(4500,980,"Dirac DM")
    leg4=TLatex(4500, 780,"#splitline{#it{g_{q} = 0.25}}{#it{g_{DM} = 1.0}}")
    leg7=TLatex(4700, 290,"#bf{Observed}")
    leg7.SetTextSize(0.050)
    leg6=TLatex(4700, 100,"#bf{Expected}")
    leg6.SetTextSize(0.050)
    leg1.SetTextFont(42)
    leg4.SetTextFont(42)
    leg5.SetTextFont(42)
    leg1.SetTextSize(0.040)
    leg4.SetTextSize(0.040)
    leg5.SetTextSize(0.040)
    leg6.Draw("same")
    leg7.Draw("same")
    leg4.Draw("same")
    leg5.Draw("same")
    leg8 = TLine(4500,320,4650,320)
    leg8.SetLineColor(kAzure)
    leg8.SetLineWidth(2)
    leg8.Draw("same")
    leg9 = TLine(4500,125,4650,125)
    leg9.SetLineColor(kAzure+1)
    leg9.SetLineWidth(2)
    leg9.SetLineStyle(2)
    leg9.Draw("same")
    leg11 = TLatex(4500,450,"#bf{Dijet "+CL+"% CL}")
    leg11.SetTextSize(0.050)
    leg11.Draw("same")


elif Mediator=="Axial" and DijetOnly:
    leg1=TLatex(4300, 1010,Mediator+"-vector mediator")
    leg5=TLatex(4300, 880,"Dirac DM")
    leg4=TLatex(4300, 680,"#splitline{#it{g_{q} = 0.25}}{#it{g_{DM} = 1.0}}")
    leg1.SetTextFont(42)
    leg4.SetTextFont(42)
    leg5.SetTextFont(42)
    leg1.SetTextSize(0.040)
    leg4.SetTextSize(0.040)
    leg5.SetTextSize(0.040)
    leg4.Draw("same")
    leg5.Draw("same")
    leg8 = TLine(4300,320,4450,320)
    leg8.SetLineColor(kAzure)
    leg8.SetLineWidth(2)
    leg8.Draw("same")
    leg9 = TLine(4300,125,4450,125)
    leg9.SetLineColor(kAzure+1)
    leg9.SetLineWidth(2)
    leg9.SetLineStyle(2)
    leg9.Draw("same")
    leg11 = TLatex(4300,450,"#bf{Dijet "+CL+"% CL}")
    leg11.SetTextSize(0.050)
    leg11.Draw("same")
    leg7=TLatex(4500, 290,"#bf{Observed}")
    leg7.SetTextSize(0.050)
    leg6=TLatex(4500, 100,"#bf{Expected}")
    leg6.SetTextSize(0.050)
    leg6.Draw("same")
    leg7.Draw("same")

elif Mediator=="Vector" and not METXonly:
    leg1=TLatex(3500,1500,"#splitline{#bf{Vector mediator}}{#bf{Dirac DM}}")
    leg4=TLatex(3500,1280,"#splitline{#it{g_{q} = 0.25}}{#it{g_{DM} = 1.0}}")
    leg1.SetTextFont(42)
    leg4.SetTextFont(42)
    #leg5.SetTextFont(42)
    leg1.SetTextSize(0.040)
    leg4.SetTextSize(0.040)
    #leg5.SetTextSize(0.040)
    leg4.Draw("same")
    #leg5.Draw("same")
elif Mediator=="Axial" and not METXonly:
    leg1=TLatex(3350, 1500,"#bf{Axial-Vector mediator}")
    leg5=TLatex(3800, 1400,"#bf{Dirac DM}")
    leg4=TLatex(3800, 1220,"#splitline{#it{g_{q} = 0.25}}{#it{g_{DM} = 1.0}}")
    leg1.SetTextFont(42)
    leg4.SetTextFont(42)
    leg5.SetTextFont(42)
    leg1.SetTextSize(0.040)
    leg4.SetTextSize(0.040)
    leg5.SetTextSize(0.040)
    leg4.Draw("same")
    leg5.Draw("same")

elif Mediator=="Vector" and METXonly:
    leg1=TLatex(1105,710,"#splitline{#bf{"+Mediator+" mediator, Dirac DM}}{#it{g_{q} = 0.25, g_{DM} = 1}}")
    leg1.SetTextFont(42)
    leg1.SetTextSize(0.030)
elif Mediator=="Axial" and METXonly:
    leg1=TLatex(1105,705,"#splitline{#bf{"+Mediator+"-vector mediator, Dirac DM}}{#it{g_{q} = 0.25, g_{DM} = 1}}")
    leg1.SetTextFont(42)
    leg1.SetTextSize(0.030)

################################
### CMS / lumi / energy text ###
################################

if logx         : 
    # CMS
    leg2=TLatex(100,1720,"#bf{CMS} #it{Preliminary}")
    leg2.SetTextFont(42)
    leg2.SetTextSize(0.045)
    # lumi
    leg3=TLatex(1500,1470,"#bf{Dark Matter Summary}")
    leg3.SetTextFont(42)
    leg3.SetTextSize(0.033)
elif Dilepton : 
    # CMS
    leg2=TLatex(100,2020,"#bf{CMS}")
    leg2.SetTextFont(42)
    leg2.SetTextSize(0.045)
    # lumi
    leg3=TLatex(3700,2020,"12.9 fb^{-1} (13 TeV)")
    leg3.SetTextFont(42)
    leg3.SetTextSize(0.045)
elif DijetOnly : 
    # CMS
    leg2=TLatex(1400,2330,"#bf{CMS} Preliminary")
    leg2.SetTextFont(42)
    leg2.SetTextSize(0.045)
    # lumi
    leg3=TLatex(4550,2330,"77.8 fb^{-1} (13 TeV)")
    leg3.SetTextFont(42)
    leg3.SetTextSize(0.045)
#elif Mediator=="Vector" and DijetOnly : 
#    # CMS
#    leg2=TLatex(100,1470,"#bf{CMS}")
#    leg2.SetTextFont(42)
#    leg2.SetTextSize(0.045)
#    # lumi
#    leg3=TLatex(2550,1470,"12.9 fb^{-1} (13 TeV)")
#    leg3.SetTextFont(42)
#    leg3.SetTextSize(0.045)
else         : 
    # CMS
    leg2=TLatex(200,1590,"#bf{CMS}")
    leg2.SetTextFont(42)
    leg2.SetTextSize(0.045)
    # lumi
    leg3=TLatex(2450,1720,"13 fb^{-1}, 27 fb^{-1} & 36 fb^{-1} (13 TeV)")
    leg3.SetTextFont(42)
    leg3.SetTextSize(0.045)

############
### Draw ###
############/

for analysis in analyses:
    if not  analysis=="relic":
	continue
        le=leg.AddEntry(tgraph[analysis],text[analysis])
	le.SetTextSize(0.02)
	le.SetTextAlign(13)
if Mediator=="Axial" and not METXonly and not DijetOnly and not Dilepton:
  le=leg.AddEntry(tgraph["monotop"],text["monotop"])
  le.SetTextSize(0.02)
  le.SetTextAlign(13)

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
            tgraph["relic"].SetLineColor(color[analysis]-1)
            tgraph["relic"].SetFillColor(color[analysis]-1)
            tgraph["relic"].SetLineStyle(linestyle[analysis])
            tgraph["relic"].SetLineWidth(-202)#was 202
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


if Mediator=="Axial" and not METXonly and not DijetOnly and not Dilepton:
  tpad = TPad("p2" ,"",0.6500,0.1200,0.8600,0.5000,0,0,0)
  tpad.Draw()

  tline1 = TLine(3370, 805, 3550, 805);
  tline1.SetLineColor(kAzure)
  tline1.SetLineWidth(202)
  tline1.SetLineStyle(kSolid)
  tline1.Draw()

  tline2 = TLine(3370, 635, 3550, 635);
  tline2.SetLineColor(kAzure+1)
  tline2.SetLineWidth(202)
  tline2.SetLineStyle(kSolid)
  tline2.Draw()

  tline3 = TLine(3370, 485, 3550, 485);
  tline3.SetLineColor(kRed+1)
  tline3.SetLineWidth(202)
  tline3.SetLineStyle(kSolid)
  tline3.Draw()

  tline4 = TLine(3370, 321, 3550, 321);
  tline4.SetLineColor(kGreen+3)
  tline4.SetLineWidth(202)
  tline4.SetLineStyle(kSolid)
  tline4.Draw()

  tline5 = TLine(3370, 155, 3550, 155);
  tline5.SetLineColor(kOrange-3)
  tline5.SetLineWidth(202)
  tline5.SetLineStyle(kSolid)
  tline5.Draw()



  leg6=TLatex(3580, 780, "#bf{#scale[0.7]{Dijet}} #scale[0.5]{#it{[EXO-265056]}}")
  leg6.SetTextFont(42)
  leg6.Draw()

  leg7=TLatex(3580, 615, "#bf{#scale[0.7]{Boosted Dijet}} #scale[0.5]{#it{[EXO-16-030]}}")
  leg7.SetTextFont(42)
  leg7.Draw()

  leg8=TLatex(3580, 460, "#bf{#scale[0.7]{DM + j/V_{qq}}} #scale[0.5]{#it{[EXO-16-037]}}")
  leg8.SetTextFont(42)
  leg8.Draw()

  leg9=TLatex(3580, 300, "#bf{#scale[0.7]{DM + #gamma}} #scale[0.5]{#it{[EXO-16-039]}}")
  leg9.SetTextFont(42)
  leg9.Draw()

  leg10=TLatex(3580, 125, "#bf{#scale[0.7]{DM + Z_{ll}}} #scale[0.5]{#it{[EXO-16-038]}}")
  leg10.SetTextFont(42)
  leg10.Draw()


elif Mediator=="Vector" and not METXonly and not DijetOnly and not Dilepton:

  tpad = TPad("p2" ,"",0.6500,0.1200,0.8600,0.4500,0,0,0)
  tpad.Draw()

  tline1 = TLine(3370, 675, 3550, 675);
  tline1.SetLineColor(kAzure)
  tline1.SetLineWidth(202)
  tline1.SetLineStyle(kSolid)
  tline1.Draw()

  tline2 = TLine(3370, 545, 3550, 545);
  tline2.SetLineColor(kAzure+1)
  tline2.SetLineWidth(202)
  tline2.SetLineStyle(kSolid)
  tline2.Draw()

  tline3 = TLine(3370, 415, 3550, 415);
  tline3.SetLineColor(kRed+1)
  tline3.SetLineWidth(202)
  tline3.SetLineStyle(kSolid)
  tline3.Draw()

 # tline6 = TLine(3370, 415, 3550, 415);
 # tline6.SetLineColor(kViolet)
 # tline6.SetLineWidth(202)
 # tline6.SetLineStyle(kDashed)
 # tline6.Draw()

  tline4 = TLine(3370, 281, 3550, 281);
  tline4.SetLineColor(kGreen+3)
  tline4.SetLineWidth(202)
  tline4.SetLineStyle(kSolid)
  tline4.Draw()

  tline5 = TLine(3370, 155, 3550, 155);
  tline5.SetLineColor(kOrange-3)
  tline5.SetLineWidth(202)
  tline5.SetLineStyle(kSolid)
  tline5.Draw()

  leg6=TLatex(27500, 300, "Observed")
  leg6.SetTextFont(42)
  leg6.Draw()

  leg7=TLatex(3580, 518, "#bf{#scale[0.7]{Boosted Dijet}} #scale[0.5]{#it{[EXO-16-030]}}")
  leg7.SetTextFont(42)
  leg7.Draw()

  leg8=TLatex(3580, 387, "#bf{#scale[0.7]{DM + j/V_{qq}}} #scale[0.5]{#it{[EXO-16-037]}}")
  leg8.SetTextFont(42)
  leg8.Draw()

#  leg11=TLatex(3580, 387, "#bf{#scale[0.7]{DM + t}} #scale[0.5]{#it{[EXO-16-040]}}")
#  leg11.SetTextFont(42)
#  leg11.Draw()

  leg9=TLatex(3580, 256, "#bf{#scale[0.7]{DM + #gamma}} #scale[0.5]{#it{[EXO-16-039]}}")
  leg9.SetTextFont(42)
  leg9.Draw()

  leg10=TLatex(3580, 125, "#bf{#scale[0.7]{DM + Z_{ll}}} #scale[0.5]{#it{[EXO-16-038]}}")
  leg10.SetTextFont(42)
  leg10.Draw()

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
