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

################
### Settings ###
################

Mediator = raw_input('Choose Mediator [Scalar or Pseudo]: ')
ObsOnly  = ast.literal_eval(raw_input('Obs only? [True or False]: '))

#################
### Analyses ####
#################

analyses = ["BSM",
            "monojet_obs",
            "DMtt_obs",
            #"METbb_DMtt_obs",
            "METbb_DMbb_obs"
            #,"METbb_DMhf_obs"
            ]

if not ObsOnly: analyses=["BSM",
                          "monojet_obs",   "monojet_exp",
                          "DMtt_obs",      "DMtt_exp",
                          "METbb_DMbb_obs","METbb_DMbb_exp"
                          #"METbb_DMtt_exp","METbb_DMtt_obs",
                          #"METbb_DMhf_exp","METbb_DMhf_obs",
                          ]

tgraph    = {}
color     = {}
text      = {}
filepath  = {}
linestyle = {}

############# 
### Files ###
#############

if Mediator == "Scalar":
    filepath["monojet_obs"]    = "Monojet/ScanMM/limit_1D_s_fermion.root"
    filepath["monojet_exp"]    = "Monojet/ScanMM/limit_1D_s_fermion.root"
    filepath["DMtt_obs"]       = "DMtt/DMtt_Scalar_ICHEP2016_Mx_obs.txt"
    filepath["DMtt_exp"]       = "DMtt/DMtt_Scalar_ICHEP2016_Mx_exp.txt"
    filepath["METbb_DMtt_obs"] = "DMbb/2015/Limits_hfDMs.root"
    filepath["METbb_DMbb_obs"] = "DMbb/2015/Limits_hfDMs.root"
    filepath["METbb_DMhf_obs"] = "DMbb/2015/Limits_hfDMs.root"
    filepath["METbb_DMtt_exp"] = "DMbb/2015/Limits_hfDMs.root"
    filepath["METbb_DMbb_exp"] = "DMbb/2015/Limits_hfDMs.root"
    filepath["METbb_DMhf_exp"] = "DMbb/2015/Limits_hfDMs.root"
if Mediator == "Pseudo":
    filepath["monojet_obs"]    = "Monojet/ScanMM/limit_1D_ps.root"
    filepath["monojet_exp"]    = "Monojet/ScanMM/limit_1D_ps.root"
    filepath["DMtt_obs"]       = "DMtt/DMtt_Pseudo_ICHEP2016_Mx_obs.txt"
    filepath["DMtt_exp"]       = "DMtt/DMtt_Pseudo_ICHEP2016_Mx_exp.txt"
    filepath["METbb_DMtt_obs"] = "DMbb/2015/Limits_hfDMps.root"
    filepath["METbb_DMbb_obs"] = "DMbb/2015/Limits_hfDMps.root"
    filepath["METbb_DMhf_obs"] = "DMbb/2015/Limits_hfDMps.root"
    filepath["METbb_DMtt_exp"] = "DMbb/2015/Limits_hfDMps.root"
    filepath["METbb_DMbb_exp"] = "DMbb/2015/Limits_hfDMps.root"
    filepath["METbb_DMhf_exp"] = "DMbb/2015/Limits_hfDMps.root"

#######################
### Plot linestyles ###
#######################

linestyle["BSM" ]           = kDotted
#MET+jets
linestyle["monojet_obs"]    = kSolid
linestyle["monojet_exp"]    = kDashed
# HF
linestyle["DMtt_obs"]       = kSolid
linestyle["METbb_DMtt_obs"] = kSolid
linestyle["METbb_DMbb_obs"] = kSolid
linestyle["METbb_DMhf_obs"] = kSolid
linestyle["DMtt_exp"]       = kDashed
linestyle["METbb_DMtt_exp"] = kDashed
linestyle["METbb_DMbb_exp"] = kDashed
linestyle["METbb_DMhf_exp"] = kDashed

###################
### Plot colors ###
###################

color["BSM"]            = kBlack
color["monojet_obs"]    = kRed+1
color["DMtt_obs"]       = kGreen+2
color["METbb_DMbb_obs"] = kGreen+1
##
color["METbb_DMhf_obs"] = kAzure+2
color["METbb_DMtt_obs"] = kAzure+2
##
color["monojet_exp"]    = color["monojet_obs"]
color["DMtt_exp"]       = color["DMtt_obs"]
color["METbb_DMbb_exp"] = color["METbb_DMbb_obs"]
color["METbb_DMtt_exp"] = color["METbb_DMtt_obs"]
color["METbb_DMhf_exp"] = color["METbb_DMhf_obs"]

##################
### Plot texts ###
##################

text["BSM"]            = "#sigma_{theory} (LHC DM WG)"
if   Mediator == "Scalar": text["monojet_obs"] = "DM + j/V_{qq} (12.9 fb^{-1})"
elif Mediator == "Pseudo": text["monojet_obs"] = "DM + j/V_{qq} (12.9 fb^{-1}) #it{EXO-16-037}"
text["DMtt_obs"]       = "DM + tt (2.2 fb^{-1}) #it{EXO-16-005}"
text["METbb_DMbb_obs"] = "DM + bb (2.2 fb^{-1}) #it{B2G-15-007}"
text["METbb_DMtt_obs"] = "DM + tt (nj<4) [B2G-15-007]"
text["METbb_DMhf_obs"] = "MET+bb: DM+HF [B2G-15-007]"
#exp
text["monojet_exp"]    = "exp.excl 95%CL"
text["DMtt_exp"]       = "exp.excl 95%CL"
text["METbb_DMbb_exp"] = "exp.excl 95%CL"
text["METbb_DMtt_exp"] = "exp.excl 95%CL"
text["METbb_DMhf_exp"] = "exp.excl 95%CL"

text["gen_obs"] = "Observed exclusion 95% CL"
text["gen_exp"] = "Expected exclusion 95% CL"

####################
### Get datfiles ###
### Get graphs   ###
####################

f1 = TF1("f1","1",0,1000)

for analysis in analyses: 
    if   analysis == "BSM"            : tgraph[analysis] = TGraph(f1)
    elif analysis == "monojet_obs"    : tgraph[analysis] = TFile(filepath[analysis]).Get("obs")
    elif analysis == "monojet_exp"    : tgraph[analysis] = TFile(filepath[analysis]).Get("exp")
    elif analysis == "METbb_DMbb_obs" : tgraph[analysis] = TFile(filepath[analysis]).Get("bbObs0s")
    elif analysis == "METbb_DMtt_obs" : tgraph[analysis] = TFile(filepath[analysis]).Get("ttObs0s")
    elif analysis == "METbb_DMhf_obs" : tgraph[analysis] = TFile(filepath[analysis]).Get("hfObs0s")
    elif analysis == "METbb_DMbb_exp" : tgraph[analysis] = TFile(filepath[analysis]).Get("bbExp0s")
    elif analysis == "METbb_DMtt_exp" : tgraph[analysis] = TFile(filepath[analysis]).Get("ttExp0s")
    elif analysis == "METbb_DMhf_exp" : tgraph[analysis] = TFile(filepath[analysis]).Get("hfExp0s")
    else                              : tgraph[analysis] = TGraph(filepath[analysis])

###################
### Make Canvas ###
### Set ranges  ###
###################

C=TCanvas("C","C",750,600)
C.cd(1).SetLogx()
C.cd(1).SetLogy()

tgraph["monojet_obs"].SetTitle("")
tgraph["monojet_obs"].GetXaxis().SetTitle("M_{Med} [GeV]")
tgraph["monojet_obs"].GetYaxis().SetTitle("#sigma / #sigma_{theory}")
tgraph["monojet_obs"].GetXaxis().SetTitleOffset(1.0)
tgraph["monojet_obs"].GetYaxis().SetTitleOffset(1.0)
tgraph["monojet_obs"].GetXaxis().SetTitleSize(0.045)
tgraph["monojet_obs"].GetYaxis().SetTitleSize(0.045)
tgraph["monojet_obs"].GetXaxis().SetRangeUser(10,    500)
tgraph["monojet_obs"].GetYaxis().SetRangeUser(0.1, 100000)
tgraph["monojet_obs"].Draw()

##################
### Add legend ###
##################

if Mediator == "Scalar": 
    tex1=TLatex(130, 40000, "#bf{Scalar mediator}")
if Mediator == "Pseudo": 
    tex1=TLatex(130, 40000, "#bf{Pseudoscalar mediator}")

tex2=TLatex(130, 20000, "#bf{Dirac DM}, #it{m_{DM} = 1 GeV}")
tex3=TLatex(130, 11000, "#it{g_{q} = 1, g_{DM} = 1}")

tex1.SetTextFont(42)
tex2.SetTextFont(42)
tex3.SetTextFont(42)
tex1.SetTextSize(0.03)
tex2.SetTextSize(0.03)
tex3.SetTextSize(0.03)
tex1.Draw("same")
tex2.Draw("same")
tex3.Draw("same")

if Mediator == "Scalar": leg=C.BuildLegend(0.21,0.59,0.55,0.88)
if Mediator == "Pseudo": leg=C.BuildLegend(0.21,0.62,0.55,0.88)
leg.SetBorderSize(0)
leg.SetTextFont(42)
leg.Clear()

leg2=C.BuildLegend(0.10,0.905,0.90,0.955)
leg2.SetBorderSize(0)
leg2.SetTextFont(42)
leg2.SetFillColor(0)
leg2.Clear()
leg2.SetHeader("#bf{CMS} #it{Preliminary}")

leg3=C.BuildLegend(0.74,0.905,1.54,0.955)
leg3.SetBorderSize(0)
leg3.SetTextFont(42)
leg3.SetFillColor(0)
leg3.Clear()
leg3.SetHeader("#it{ICHEP 2016}")

############
### Draw ###
############

for analysis in analyses:
    tgraph[analysis].SetLineColor(color[analysis])
    if analysis == "BSM" or analysis=="DMtt_exp" or analysis=="METbb_DMtt_exp" or analysis=="METbb_DMbb_exp" or analysis=="METbb_DMhf_exp" or analysis=="monojet_exp":
        tgraph[analysis].SetLineWidth( 3)
        tgraph[analysis].SetFillStyle(3005)
        tgraph[analysis].SetFillColor(kWhite)
    else:
        tgraph[analysis].SetFillColor(color[analysis])
        tgraph[analysis].SetFillStyle(3005)
        tgraph[analysis].SetLineWidth( 203)
    tgraph[analysis].SetLineStyle(linestyle[analysis])

dummy1 = TGraph("dummy_100.dat")
dummy2 = TGraph("dummy_600.dat")

tgraph["gen_obs"]=dummy1
tgraph["gen_exp"]=dummy2

for analysis in ["gen_obs","gen_exp"]:
        tgraph[analysis].SetLineWidth( 3)
        tgraph[analysis].SetFillStyle(3005)
        tgraph[analysis].SetLineColor(kGray)
        tgraph[analysis].SetMarkerSize(0.1)
        tgraph[analysis].SetMarkerColor(kGray)
        tgraph[analysis].SetFillColor(kGray)
        tgraph[analysis].SetLineWidth( 404)
    
tgraph["gen_exp"].SetFillColor(kWhite)
tgraph["gen_exp"].SetLineStyle(kDashed)
    
tgraph["fermion"] = tgraph["BSM"].Clone()
tgraph["fermion"].SetLineColor(kWhite)
text["fermion"] = "fermion only #it{EXO-16-037}"

if   Mediator == "Scalar":
    for analysis in ["gen_obs","gen_exp","METbb_DMbb_obs","DMtt_obs","monojet_obs","fermion","BSM"]:
        leg.AddEntry(tgraph[analysis],text[analysis])
elif Mediator == "Pseudo":
    for analysis in ["gen_obs","gen_exp","METbb_DMbb_obs","DMtt_obs","monojet_obs","BSM"]:
        leg.AddEntry(tgraph[analysis],text[analysis])

leg.Draw()
leg2.Draw()
leg3.Draw()
C.Update()
for analysis in analyses:
    tgraph[analysis].Draw("same")
C.Update()

############
### Save ###
############

if ObsOnly: C.SaveAs(Mediator+"_METX_Summary_ICHEP_obsonly.pdf")
else      : C.SaveAs(Mediator+"_METX_Summary_ICHEP_obsnexp.pdf")

###########
### FIN ###
###########
