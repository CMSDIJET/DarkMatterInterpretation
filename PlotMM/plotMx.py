#######################################
#########################################
###                                   ###
### Draw awesome MET+X Summary plots  ###
###                                   ###
### SI/SD                             ###
###                                   ###
### (c) MET+X Combo                   ###
###                                   ###
#########################################
#########################################

from ROOT import *
import ast
#DijetOnly = True
from Utilities import extrapolation 

#DijetOnly = False, Tyler files for dijet
#from Utilities2 import extrapolation


################
### Settings ###
################
TextonPlot = True

DijetOnly = False

DDresult = raw_input('Choose DD [SI or SD]: ')
METless  = ast.literal_eval(raw_input('MET-less? [True or False]: '))
if METless: DijetOnly = ast.literal_eval(raw_input('Dijet only? [True or False]: '))


#tested w/ EXO-16-32/056 and trijet 
# DDresult  = "SI"
# DijetOnly = True
# METless   = True


#tested for SI, SD 
#DDresult  = "SD"
#DijetOnly = False
#METless   = True

Extend    = True
vFloor    = False
mDM_lb = 1

#################
### Analyses ####
#################

if   DDresult == "SI": 
    metx    = ["monojet","monophoton","monoZ"]
    metless = ["dijet","trijet"]
elif DDresult == "SD": 
    metx    = ["monojet","monophoton","monoZ"]
    metless = ["dijet","trijet"]

cmsanalyses = metx
if METless  : cmsanalyses = metx+metless
if DijetOnly: 
    metless = ["dijet_2016"]
    cmsanalyses = metless


if   DDresult == "SI" and DijetOnly : analyses = cmsanalyses+["Cresst","CDMSlite","PandaX","LUX"]
#elif DDresult == "SD" and DijetOnly : analyses = cmsanalyses+["Pico2L","Pico60","SuperK","IceCube"]
elif DDresult == "SD" and DijetOnly : analyses = cmsanalyses+["PICASSO", "Pico60","SuperKbb","IceCubebb", "IceCubett"]
elif DDresult == "SI"               : analyses = ["Cresst","CDMSlite","PandaX","LUX"]+cmsanalyses
#elif DDresult == "SD"               : analyses = ["Pico2L","Pico60","SuperK","IceCube"]+cmsanalyses
elif DDresult == "SD"               : analyses = ["PICASSO", "Pico60","SuperKbb","IceCubebb", "IceCubett"]+cmsanalyses

if vFloor: analyses += ["vFloor"]

print "***********************"
print "DD result = ", DDresult
print "List of analyses = ", analyses
print "***********************"

if Extend :
    print "*******************"
    print "N.B: METX analyses = " , metx 
    print "will be extended downto MDM = " , mDM_lb
    print "*******************"

tgraph    = {}
tgraph_original    = {}
DDgraph   = {}
#if Extend : DDgraph_extr   = {}
color     = {}
text      = {}
filepath  = {}
linestyle = {}

############# 
### Files ###
#############

if DDresult == "SI":
    filepath["LUX"]            = "DD/SI/LUX_SI_Combination_Oct2016.txt"#"DD/SI/LUX_SI_DMTools_Jul2016.dat"#"DD/lux2015.txt"
    filepath["PandaX"]         = "DD/SI/pandax.txt"                 
    filepath["CDMSlite"]       = "DD/SI/cdmslite2015.txt"
    filepath["Cresst"]         = "DD/SI/cresstii.txt"
    filepath["vFloor"]         = "DD/SI/Neutrino_SI.txt"
    ### ICHEP
#    filepath["dijet"]          = "Dijet/ScanMM/MMedMDM_dijet_v_90_Phil500.root"
#from Tyler EXO-16-056
    filepath["dijet"]          = "Dijet/ScanMM/Dijet_MM_V_Dijetpaper2016_obs_90.root"
    ### Dijet paper
    #filepath["dijet_2016"]     = "Dijet/ScanMM/MMedMDM_dijet_v_90_Phil600.root"
    #filepath["dijet_2016_exp"] = "Dijet/ScanMM/MMedMDM_dijet_v_90_Phil600.root"

#    filepath["dijet_2016"]     = "Dijet/ScanMM/MMedMDM_dijet_v_90_top56.root"
#    filepath["dijet_2016_exp"] = "Dijet/ScanMM/MMedMDM_dijet_v_90_top56.root"    
    filepath["dijet_2016"]          = "Dijet/ScanMM/Dijet_MM_V_Dijetpaper2016_obs_90.root"
    filepath["dijet_2016_exp"]          = "Dijet/ScanMM/Dijet_MM_V_Dijetpaper2016_obs_90.root"



    filepath["trijet"]         = "Trijet/ScanMM/MMedMDM_v_90.root"
    filepath["monojet"]        = "Monojet/ScanMM/vector_g025_DD.root"
    filepath["monophoton"]     = "Monophoton/ScanMM/Monophoton_SI_MM_ICHEP2016_obs.root"
    #2015: filepath["monoZ"]   = "MonoZll/ScanMM/monoz_vector_gq0p25_cl90_2015.txt"
    filepath["monoZ"]          = "MonoZll/ScanMM/monoz_exo16038_si.txt"
elif DDresult == "SD" :
    # filepath["Pico2L"]         = "DD/SD/Pico2L.txt"
    # filepath["Pico60"]         = "DD/SD/Pico60.txt"
    # filepath["SuperK"]         = "DD/SD/SuperKtautau.txt"
    # filepath["IceCube"]        = "DD/SD/IceCubetautau.txt"

    # filepath["PICASSO"]         = "Pico60/PicassoFinal.root"
    # filepath["Pico60"]         = "Pico60/Pico602017.root"
    # filepath["SuperKbb"]      = "Pico60/Neutrino.root"
    # filepath["IceCubebb"]     = "Pico60/Neutrino.root"
    # filepath["IceCubett"]     = "Pico60/Neutrino.root"

    filepath["PICASSO"]         = "DirectDetection/PicassoFinal.root"
    filepath["Pico60"]         = "DirectDetection/Pico602017.root"
    filepath["SuperKbb"]      = "DirectDetection/SuperKbb.root"
    filepath["IceCubebb"]     = "DirectDetection/IceCubebb.root"
    filepath["IceCubett"]     = "DirectDetection/IceCubett.root"
    filepath["vFloor"]         = "DD/SD/Neutrino_SD.txt"
    ### ICHEP
#    filepath["dijet"]          = "Dijet/ScanMM/MMedMDM_dijet_av_90_Phil500.root"
#from Tyler EXO-16-056
    filepath["dijet"]          = "Dijet/ScanMM/Dijet_MM_A_Dijetpaper2016_obs_90.root" 
    ### Dijet paper
    #filepath["dijet_2016"]     = "Dijet/ScanMM/MMedMDM_dijet_av_90_Phil600.root"
    #filepath["dijet_2016_exp"] = "Dijet/ScanMM/MMedMDM_dijet_av_90_Phil600.root"
    
    #filepath["dijet_2016"]     = "Dijet/ScanMM/MMedMDM_dijet_av_90_top56.root"    
    #filepath["dijet_2016_exp"] = "Dijet/ScanMM/MMedMDM_dijet_av_90_top56.root"
    filepath["dijet_2016"]          = "Dijet/ScanMM/Dijet_MM_A_Dijetpaper2016_obs_90.root"
    filepath["dijet_2016_exp"]          = "Dijet/ScanMM/Dijet_MM_A_Dijetpaper2016_obs_90.root"
    filepath["trijet"]         = "Trijet/ScanMM/MMedMDM_av_90.root"
    filepath["monojet"]        = "Monojet/ScanMM/axial_g025_DD.root"
    filepath["monophoton"]     = "Monophoton/ScanMM/Monophoton_SD_MM_ICHEP2016_obs.root"
    #2015: filepath["monoZ"]   = "MonoZll/ScanMM/monoz_axial_gq0p25_cl90_2015.txt"
    filepath["monoZ"]          = "MonoZll/ScanMM/monoz_exo16038_sd.txt"

#######################
### Plot linestyles ###
#######################

linestyle["vFloor"]     = kDashed
### SI
linestyle["LUX"]        = kSolid
linestyle["PandaX"]     = kSolid
linestyle["CDMSlite"]   = kSolid
linestyle["Cresst"]     = kSolid
### SD
# linestyle["Pico2L"]     = kSolid
# linestyle["Pico60"]     = kSolid
# linestyle["SuperK"]     = kDashed
# linestyle["IceCube"]    = kDashed
linestyle["PICASSO"]     = kSolid
linestyle["Pico60"]     = kSolid
linestyle["SuperKbb"]     = kSolid
linestyle["IceCubebb"]     = kSolid
linestyle["IceCubett"]     = kSolid
### CMS Met-less
linestyle["dijet"]      = kSolid
linestyle["dijet_2016"] = kSolid
linestyle["trijet"]     = kSolid
### CMS MET+X
linestyle["monophoton"] = kSolid
linestyle["monoZ"]      = kSolid
linestyle["monotop"]    = kSolid
linestyle["monojet"]    = kSolid

###################
### Plot colors ###
###################

color["vFloor"]     = kOrange+3
### SI
color["Cresst"]     = kGreen+1
color["CDMSlite"]   = kGreen+3
color["PandaX"]     = kGreen+2
color["LUX"]        = kGreen+4
### SD
# color["Pico2L"]     = kGreen+1
# color["Pico60"]     = kGreen+3
# color["SuperK"]     = kGreen+2
# color["IceCube"]    = kGreen+4
color["PICASSO"]     = kBlack
color["Pico60"]     = kGreen+1
color["SuperKbb"]     = kGreen+3
color["IceCubebb"]     = kGreen+2
color["IceCubett"]     = kGreen
### CMS Met-less
color["dijet"]      = kAzure
color["dijet_2016"] = kAzure
color["trijet"]     = kAzure+1
color["chi"]        = kBlue
### CMS MET+X
color["monojet"]    = kRed+1#kRed+1
color["monophoton"] = kOrange+10#kRed+2
color["monoZ"]      = kOrange-3#kRed+3
color["monotop"]    = kViolet+1

##################
### Plot texts ###
##################

text["vFloor"]     = "#nu floor (permeable)"
### SI
text["LUX"]        = "LUX"
text["PandaX"]     = "PandaX-II"
text["CDMSlite"]   = "CDMSlite"
text["Cresst"]     = "CRESST-II"
### SD
#text["Pico2L"]     = "PICO-2L"
#text["Pico60"]     = "PICO-60"
#text["SuperK"]     = "Super-K (#tau^{+}#tau^{-})"
#text["IceCube"]    = "IceCube (#tau^{+}#tau^{-})"
text["PICASSO"]     = "PICASSO"
text["Pico60"]      = "PICO-60"
text["SuperKbb"]    = "Super-K (b#bar{b})"
text["IceCubebb"]   = "IceCube (b#bar{b})"
text["IceCubett"]   = "IceCube (t#bar{t})"
### CMS MET-less
if DDresult=="SD" :
    text["dijet"]      = "CMS Dijet [EXO-16-056]"
else :
    text["dijet"]      = "#splitline{CMS Dijet}{[EXO-16-056]}"
text["dijet_2016"] = "CMS Dijet #it{[EXO-16-056]}"
text["trijet"]     = "CMS Boosted dijet #it{[EXO-16-030]}"
text["chi"]        = "chi obs. (exp.excl.)"
### CMS MET+X
text["monojet"]    = "CMS DM+j/V_{qq} #it{[EXO-16-037]}"
text["monoZ"]      = "CMS DM+Z_{ll} #it{[EXO-16-038]}"
text["monophoton"] = "CMS DM+#gamma #it{[EXO-16-039]}"
text["monotop"]    = "CMS DM+t (FC) #it{[EXO-16-040]}"

####################
### Get datfiles ###
### Get graphs   ###
####################

for analysis in analyses: 
#    if   analysis == "dijet"          : tgraph["dijet"]          = TFile(filepath[analysis]).Get("obs_025")

#from Tyler EXO-16-056
    if   analysis == "dijet"          : tgraph["dijet"]          = TFile(filepath[analysis]).Get("Obs_90")
  
    #elif analysis == "dijet_2016"     : tgraph["dijet_2016"]     = TFile(filepath[analysis]).Get("obs_025")  
    #elif analysis == "dijet_2016_exp" : tgraph["dijet_2016_exp"] = TFile(filepath[analysis]).Get("exp_025")  
    elif analysis == "dijet_2016"     : tgraph["dijet_2016"]     = TFile(filepath[analysis]).Get("Obs_90")  
    elif analysis == "dijet_2016_exp" : tgraph["dijet_2016_exp"] = TFile(filepath[analysis]).Get("Obs_90")  

    elif analysis == "trijet"         : tgraph["trijet"]         = TFile(filepath[analysis]).Get("obs_025")  
    elif analysis == "monojet"        : tgraph["monojet"]        = TFile(filepath[analysis]).Get("observed")
    elif analysis == "monophoton"     : tgraph["monophoton"]     = TFile(filepath[analysis]).Get("monophoton_obs")
    elif analysis == "monotop"        : tgraph["monotop"]        = TFile(filepath[analysis]).Get("observed")
    # elif analysis == "PICASSO"        : tgraph["PICASSO"]        = TFile(filepath[analysis]).Get("Graph")
    # elif analysis == "Pico60"         : tgraph["Pico60"]         = TFile(filepath[analysis]).Get("Graph")
    # elif analysis == "SuperKbb"       : tgraph["SuperKbb"]       = TFile(filepath[analysis]).Get("Superk_bb")
    # elif analysis == "IceCubebb"      : tgraph["IceCubebb"]      = TFile(filepath[analysis]).Get("IC_bb_Dec2016")
    # elif analysis == "IceCubett"      : tgraph["IceCubett"]      = TFile(filepath[analysis]).Get("Icecube_toptop")
    elif analysis == "PICASSO"        : tgraph["PICASSO"]        = TFile(filepath[analysis]).Get("Obs_90")
    elif analysis == "Pico60"         : tgraph["Pico60"]         = TFile(filepath[analysis]).Get("Obs_90")
    elif analysis == "SuperKbb"       : tgraph["SuperKbb"]       = TFile(filepath[analysis]).Get("Obs_90")
    elif analysis == "IceCubebb"      : tgraph["IceCubebb"]      = TFile(filepath[analysis]).Get("Obs_90")
    elif analysis == "IceCubett"      : tgraph["IceCubett"]      = TFile(filepath[analysis]).Get("Obs_90")
    else                              : tgraph[analysis]         = TGraph(filepath[analysis])

#######################
### Transform 90%CL ###
### to DD plane     ###
#######################

if DDresult=="SI":
    #c_SI = 0.3984e-27*(9./3.14159) #gq=1
    c_SI = 6.9e-41*1e12
    for analysis in cmsanalyses:
        DDgraph[analysis]=TGraph()
        for i in range(0,tgraph[analysis].GetN()) :
            mMed = Double(0)
            mDM  = Double(0)
            tgraph[analysis].GetPoint(i,mMed,mDM)
#            print "SI - analysis = ", analysis, ", i = ", i, ", mMed = ", mMed, ", mDM = ", mDM
            if analysis == "monophoton":
                DDgraph[analysis].SetPoint(i,pow(10,mMed),pow(10,mDM))        
            elif analysis == "monojet" or analysis == "monoZ":
                DDgraph[analysis]=tgraph[analysis]
            else: 
                mR = Double(0.939*mDM)/(0.939+mDM)
                xsec = Double(c_SI*(mR*mR)/(mMed*mMed*mMed*mMed))
#                print "x-sec = ", xsec
                DDgraph[analysis].SetPoint(i,mDM,xsec)        
        tgraph[analysis] = DDgraph[analysis]
elif DDresult=="SD":
    #c_SD = 4.6*1e-29  #gq=1
    c_SD = 2.4e-42*1e12
    for analysis in cmsanalyses:
        DDgraph[analysis]=TGraph()
        for i in range(0,tgraph[analysis].GetN()) :
            mMed = Double(1)
            mDM  = Double(1)
            tgraph[analysis].GetPoint(i,mMed,mDM)
#            print "SD - analysis = ", analysis, ", i = ", i, ", mMed = ", mMed, ", mDM = ", mDM
            if analysis == "monophoton":
                DDgraph[analysis].SetPoint(i,pow(10,mMed),pow(10,mDM))        
            elif analysis == "monojet" or analysis == "monoZ":
                DDgraph[analysis]=tgraph[analysis]
            else: 
                mR = Double(0.939*mDM)/(0.939+mDM)
                xsec = Double(c_SD*(mR*mR)/(mMed*mMed*mMed*mMed))
 #               print "x-sec = ", xsec
                DDgraph[analysis].SetPoint(i,mDM,xsec)        
        tgraph[analysis] = DDgraph[analysis]

    print "****BEFORE EXTRAPOLATIOn*****"
    for analysis in cmsanalyses :
#        print "Analysis ", analysis
        for i in range(0,tgraph[analysis].GetN()) :
            mDM_i  = Double(0)  
            xsec_i = Double(0)    
            tgraph[analysis].GetPoint(i,mDM_i,xsec_i)
#            print "i = ", i, " mDM_i = ", mDM_i, "xsec_i = ", xsec_i
    print "*********"


if Extend :
#DijetOnly = True
#    extrapolation( tgraph, DijetOnly, cmsanalyses, metx, metless, mDM_lb )
#DijetOnly = False 
    #extrapolation( tgraph, DijetOnly, cmsanalyses, metless, mDM_lb )
    print(metless)
    extrapolation( tgraph, DijetOnly, metless, metx, mDM_lb )

###################
### Make Canvas ###
### Add legend  ###
###################

if not DijetOnly:
    C=TCanvas("C","C",600,600)
    C.Divide(1)
    C.cd(1).SetPad(0.0,0,1.0,1.0)
    C.cd(1).SetLeftMargin(0.15)
    C.cd(1).SetRightMargin(0.05)
else :
    C=TCanvas("C","C",600,600)
    C.Divide(1)
    C.cd(1).SetPad(0.0,0,1.0,1.0)
    C.cd(1).SetLeftMargin(0.15)
    C.cd(1).SetRightMargin(0.05)

C.cd(1).SetLogx()
C.cd(1).SetLogy()

if   DDresult=="SD" and DijetOnly : frame = C.cd(1).DrawFrame(mDM_lb,1e-44,1450,1e-37)
#elif DDresult=="SD"               : frame = C.cd(1).DrawFrame(0.1,1e-45,1450,1e-37) 
elif DDresult=="SD"               : frame = C.cd(1).DrawFrame(mDM_lb,1e-44,1450,1e-37) 
elif DDresult=="SI" and DijetOnly : frame = C.cd(1).DrawFrame(mDM_lb,1e-47,1450,1e-37) 
#elif DDresult=="SI"               : frame = C.cd(1).DrawFrame(0.9,1e-50,1450,1e-35) 
elif DDresult=="SI"               : frame = C.cd(1).DrawFrame(mDM_lb,1e-47,1450,1e-35) 


C.cd(1).SetTickx()
C.cd(1).SetTicky()

frame.SetXTitle("m_{DM} [GeV]")
if   DDresult=="SD": frame.SetYTitle("#sigma^{SD}_{DM-proton} [cm^{2}]")
elif DDresult=="SI": frame.SetYTitle("#sigma^{SI}_{DM-nucleon} [cm^{2}]")
#frame.GetXaxis().SetLabelSize(0.05)
#frame.GetYaxis().SetLabelSize(0.05)
frame.GetXaxis().SetTitleSize(0.045)
frame.GetYaxis().SetTitleSize(0.045)
frame.GetXaxis().SetTitleOffset(1.0)
frame.GetYaxis().SetTitleOffset(1.5)

if not DijetOnly:
    if DDresult == "SI" : leg  = TLatex(1,2.5e-33,"#it{Moriond 2017}")
    if DDresult == "SD" : leg  = TLatex(1,1.8e-35,"#it{Moriond 2017}")
    leg.SetTextFont(42)
    leg.SetTextSize(0.04)
    leg.Draw("same")
if DijetOnly:
    if DDresult == "SI" : leg  = TLatex(0.1,1.2e-38,"#bf{CMS}")
    if DDresult == "SD" : leg  = TLatex(0.1,1.2e-37,"#bf{CMS}")
    leg.SetTextFont(42)
    leg.SetTextSize(0.04)
    leg.Draw("same")

###################
### Add legend  ###
###################

if not DijetOnly and not METless:
    leg1=C.BuildLegend(0.60,0.55,0.85,0.85)
    leg1.SetBorderSize(0)
    leg1.SetTextFont(42)
    leg1.Clear()
    if DDresult=="SI":
        leg1.SetHeader("#splitline{#bf{CMS} observed exclusion 90% CL}{Vector med., Dirac DM; g_{q} = 0.25, g_{DM} = 1.0}")
    elif DDresult=="SD":
        leg1.SetHeader("#splitline{#bf{CMS} observed exclusion 90% CL}{Axial-vector med., Dirac DM; g_{q} = 0.25, g_{DM} = 1.0}")
    
    leg2=C.BuildLegend(0.60,0.13,0.85,0.53)
    leg2.SetBorderSize(0)
    leg2.SetTextFont(42)
    leg2.Clear()
    if   DDresult == "SI": leg2.SetHeader("#bf{DD} observed exclusion 90% CL")
    elif DDresult == "SD": leg2.SetHeader("#bf{DD/ID} observed exclusion 90% CL")

    for analysis in analyses:
        if analysis=="dijet" or analysis == "dijet_2016": leg1.AddEntry(tgraph[analysis],"#splitline{CMS dijet}{#it{[EXO-16-056]}}")
        elif analysis == "trijet"     : leg1.AddEntry(tgraph[analysis],"#splitline{CMS boosted dijet}{#it{[EXO-16-030]}}")
        elif analysis == "LUX"        : leg2.AddEntry(tgraph[analysis],"#splitline{"+text[analysis]+"}{#it{[arXiv:1608.07648]}}")#1608.07648]}}") #[arXiv:1512.03506]}}")
        elif analysis == "PandaX"     : leg2.AddEntry(tgraph[analysis],"#splitline{"+text[analysis]+"}{#it{[arXiv:1607.07400]}}")
        elif analysis == "CDMSlite"   : leg2.AddEntry(tgraph[analysis],"#splitline{"+text[analysis]+"}{#it{[arXiv:1509.02448]}}")
        elif analysis == "Cresst"     : leg2.AddEntry(tgraph[analysis],"#splitline{"+text[analysis]+"}{#it{[arXiv:1509.01515]}}")
        # elif analysis == "Pico2L"     : leg2.AddEntry(tgraph[analysis],"#splitline{"+text[analysis]+"}{#it{[arXiv:1601.03729]}}")
        # elif analysis == "Pico60"     : leg2.AddEntry(tgraph[analysis],"#splitline{"+text[analysis]+"}{#it{[arXiv:1510.07754]}}")
        # elif analysis == "IceCube"    : leg2.AddEntry(tgraph[analysis],"#splitline{"+text[analysis]+"}{#it{[arXiv:1601.00653]}}")
        # elif analysis == "SuperK"     : leg2.AddEntry(tgraph[analysis],"#splitline{"+text[analysis]+"}{#it{[arXiv:1503.04858]}}")
        elif analysis == "PICASSO"    : leg2.AddEntry(tgraph[analysis],"#splitline{"+text[analysis]+"}{#it{[arXiv:1611.01499]}}")
        elif analysis == "Pico60"     : leg2.AddEntry(tgraph[analysis],"#splitline{"+text[analysis]+"}{#it{[arXiv:1702.07666]}}")
        elif analysis == "SuperKbb"   : leg2.AddEntry(tgraph[analysis],"#splitline{"+text[analysis]+"}{#it{[arXiv:1503.04858]}}")
        elif analysis == "IceCubebb"  : leg2.AddEntry(tgraph[analysis],"#splitline{"+text[analysis]+"}{#it{[arXiv:1612.05949]}}")
        elif analysis == "IceCubett"  : leg2.AddEntry(tgraph[analysis],"#splitline{"+text[analysis]+"}{#it{[arXiv:1601.00653]}}")
        elif analysis == "monojet"    : leg1.AddEntry(tgraph[analysis],"#splitline{CMS DM+j/V_{qq}}{#it{[EXO-16-037]}}")
        elif analysis == "monoZ"      : leg1.AddEntry(tgraph[analysis],"#splitline{CMS DM+Z_{ll}}{#it{[EXO-16-038]}}")
        elif analysis == "monophoton" : leg1.AddEntry(tgraph[analysis],"#splitline{CMS DM+#gamma}{#it{[EXO-16-039]}}")
        #else                          : leg1.AddEntry(tgraph[analysis],text[analysis])

######################
### Plot SI LEGEND ###
######################
if TextonPlot :
    if not DijetOnly and not METless and DDresult=="SI":
        # SI MET+X monoZ 
        legx1  = TLatex(15,4e-40,"CMS "+text["monoZ"])
        legx1.SetTextAngle(1)
        legx1.SetTextFont(42)
        legx1.SetTextColor(color["monoZ"])
        legx1.SetTextSize(0.025)
        legx1.Draw("same")
    # SI MET+X monophoton
        legx2  = TLatex(30,6e-41,"CMS "+text["monophoton"])
        legx2.SetTextAngle(1)
        legx2.SetTextFont(42)
        legx2.SetTextColor(color["monophoton"])
        legx2.SetTextSize(0.025)
        legx2.Draw("same")
    # SI MET+X monojet    
        legx3 = TLatex(50,1e-42,"CMS "+text["monojet"])
        legx3.SetTextAngle(1)
        legx3.SetTextFont(42)
        legx3.SetTextColor(color["monojet"])
        legx3.SetTextSize(0.025)
        legx3.Draw("same")

    if DDresult=="SI" and DijetOnly:
    #Cresst Dijet
        legy1 = TLatex(7,3e-41,"#splitline{"+text["Cresst"]+"}{#it{arXiv:1509.01515}}")
        legy1.SetTextAngle(0)
        legy1.SetTextFont(42)
        legy1.SetTextColor(color["Cresst"])
        legy1.SetTextSize(0.025)
        legy1.Draw("same")
    #CDMS Dijet
        legy2 = TLatex(2.,8e-39,"#splitline{"+text["CDMSlite"]+"}{#it{arXiv:1509.02448}}")
        legy2.SetTextAngle(0)
        legy2.SetTextFont(42)
        legy2.SetTextColor(color["CDMSlite"])
        legy2.SetTextSize(0.025)
        legy2.Draw("same")
    #PandaX Dijet
        legy4 = TLatex(30,1e-45,"#splitline{"+text["PandaX"]+"}{#it{arXiv:1607.07400}}")
        legy4.SetTextAngle(0)
        legy4.SetTextFont(42)
        legy4.SetTextColor(color["PandaX"])
        legy4.SetTextSize(0.025)
        legy4.Draw("same")
    #LUX Dijet
        legy3 = TLatex(200,8.0e-47,"#splitline{"+text["LUX"]+"}{#it{arXiv:1608.07648}}")
        legy3.SetTextAngle(0)
        legy3.SetTextFont(42)
        legy3.SetTextColor(color["LUX"])
        legy3.SetTextSize(0.025)
        legy3.Draw("same")
    #Dijet
        legy5  = TLatex(100,1.3e-40,"#splitline{#bf{CMS (dijet)}}{#splitline{Vector mediator, Dirac DM}{g_{q} = 0.25, g_{DM} = 1.0}}")
        legy5.SetTextAngle(0)
        legy5.SetTextFont(42)
        legy5.SetTextColor(color["dijet"])
        legy5.SetTextSize(0.025)
        legy5.Draw("same")
    #Leg
#         legX=C.BuildLegend(0.15,0.15,0.50,0.45)
#         legX.SetBorderSize(0)
#         legX.SetFillStyle(0)
#         legX.SetTextFont(42)
#         legX.SetTextSize(0.015)
#         legX.Clear()
#         legX.SetHeader("#bf{Excluded 90% CL}")
# #        legX.AddEntry(tgraph["dijet_2016"],"#splitline{Vector med., Dirac DM}{#it{g_{q} = 0.25, g_{DM} = 1.0}}")
#         legX.AddEntry(tgraph["Cresst"]    ,"#splitline{"+text["Cresst"]+"}{#it{arXiv:1509.01515}}")
#         legX.AddEntry(tgraph["CDMSlite"]  ,"#splitline{"+text["CDMSlite"]+"}{#it{arXiv:1509.02448}}")
#         legX.AddEntry(tgraph["PandaX"]    ,"#splitline{"+text["PandaX"]+"}{#it{arXiv:1607.07400}}")
#         legX.AddEntry(tgraph["LUX"]       ,"#splitline{"+text["LUX"]+"}{#it{arXiv:1608.07648}}")##it{arXiv:1512.03506}}")

#         legX.AddEntry(tgraph["dijet_2016"],"#splitline{#bf{Vector med., Dirac DM}}{#it{g_{q} = 0.25, g_{DM} = 1}}")

#         legX.Draw("same")

    elif DDresult=="SI":
    # v Floor
        if vFloor == True :
            legy0  = TLatex(1.5,3.0e-46,"#splitline{#nu Floor (perm.)}{arXiv/1506.08309}")
            legy0.SetTextAngle(0)
            legy0.SetTextFont(42)
            legy0.SetTextColor(color["vFloor"])
            legy0.SetTextSize(0.025)
            legy0.Draw("same")

        legy1 = TLatex(2.0,2.0e-39,"#splitline{CDMSlite}{arXiv:1509.02448}")
        legy1.SetTextAngle(0)
        legy1.SetTextFont(42)
        legy1.SetTextColor(color["CDMSlite"])
        legy1.SetTextSize(0.020)
        legy1.Draw("same")
    #Cresst MET+X
        legy2 = TLatex(8,3e-41,"#splitline{Cresst}{arXiv:1509.01515}")
        legy2.SetTextAngle(0)
        legy2.SetTextFont(42)
        legy2.SetTextColor(color["Cresst"])
        legy2.SetTextSize(0.020)
        legy2.Draw("same")
    #PandaX MET+X
        legy4 = TLatex(30,7e-46,"#splitline{PandaX}{arXiv:1607.07400}")
        legy4.SetTextAngle(0)
        legy4.SetTextFont(42)
        legy4.SetTextColor(color["PandaX"])
        legy4.SetTextSize(0.020)
        legy4.Draw("same")
    #LUX MET+X
        legy3 = TLatex(100,6e-47,"#splitline{LUX}{arXiv:608.07648}")
        legy3.SetTextAngle(0)
        legy3.SetTextFont(42)
        legy3.SetTextColor(color["LUX"])
        legy3.SetTextSize(0.020)
        legy3.Draw("same")

        legx4  = TLatex(10,2e-39,text["monoZ"])
        legx4.SetTextAngle(2)
        legx4.SetTextFont(42)
        legx4.SetTextColor(color["monoZ"])
        legx4.SetTextSize(0.020)
        legx4.Draw("same")
    # SD MET+X monophoton 
        legx5  = TLatex(40,4.0e-41,text["monophoton"])
        legx5.SetTextAngle(0)
        legx5.SetTextFont(42)
        legx5.SetTextColor(color["monophoton"])
        legx5.SetTextSize(0.020)
        legx5.Draw("same")
    # SD MET+X monojet
        legx6  = TLatex(40,6.0e-42,text["monojet"])
        legx6.SetTextAngle(0)
        legx6.SetTextFont(42)
        legx6.SetTextColor(color["monojet"])
        legx6.SetTextSize(0.020)
        legx6.Draw("same")
    # SD dijet
        legx7  = TLatex(1.5,1.0e-41,text["dijet"])
        legx7.SetTextAngle(0)
        legx7.SetTextFont(42)
        legx7.SetTextColor(color["dijet"])
        legx7.SetTextSize(0.020)
        legx7.Draw("same")
    # SD trijet
        legx8  = TLatex(2,1.0e-37,text["trijet"])
        legx8.SetTextAngle(0)
        legx8.SetTextFont(42)
        legx8.SetTextColor(color["trijet"])
        legx8.SetTextSize(0.020)
        legx8.Draw("same")
    # Excluded at 90% CL
        legx9  = TLatex(5,2.3e-36,"Excluded at 90% CL")
        legx9.SetTextAngle(0)
        legx9.SetTextFont(42)
        legx9.SetTextColor(1)
        legx9.SetTextSize(0.025)
        legx9.Draw("same")

###############
### Plot SD ###
###############

    if not DijetOnly and not METless and DDresult=="SD":
        # SD MET+X monoZ 
        legx1  = TLatex(3,1e-41,"CMS "+text["monoZ"])
        legx1.SetTextAngle(5)
        legx1.SetTextFont(42)
        legx1.SetTextColor(color["monoZ"])
        legx1.SetTextSize(0.025)
        legx1.Draw("same")
    # SD MET+X monophoton 
        legx2  = TLatex(3,1.6e-42,"CMS "+text["monophoton"])
        legx2.SetTextAngle(3)
        legx2.SetTextFont(42)
        legx2.SetTextColor(color["monophoton"])
        legx2.SetTextSize(0.025)
        legx2.Draw("same")
    # SD MET+X monojet
        legx3  = TLatex(3,4.0e-44,"CMS "+text["monojet"])
        legx3.SetTextAngle(2)
        legx3.SetTextFont(42)
        legx3.SetTextColor(color["monojet"])
        legx3.SetTextSize(0.025)
        legx3.Draw("same")


    if DDresult=="SD" and DijetOnly:
        # Pico2L Dijet
#         legy1  = TLatex(150,2.7e-39,text["Pico2L"])
#         legy1.SetTextAngle(0)
#         legy1.SetTextFont(42)
#         legy1.SetTextColor(color["Pico2L"])
#         legy1.SetTextSize(0.020)
#         legy1.Draw("same")
#     # Pico60 Dijet
#         legy2  = TLatex(210,6.0e-40,text["Pico60"])
#         legy2.SetTextAngle(0)
#         legy2.SetTextFont(42)
#         legy2.SetTextColor(color["Pico60"])
#         legy2.SetTextSize(0.020)
#         legy2.Draw("same")
#     # SuperK Dijet
#         legy3  = TLatex(220,1.4e-40,text["SuperK"])
#         legy3.SetTextAngle(0)
#         legy3.SetTextFont(42)
#         legy3.SetTextColor(color["SuperK"])
#         legy3.SetTextSize(0.020)
#         legy3.Draw("same")
# # IceCube Dijet
#         legy4  = TLatex(230,4.7e-41,text["IceCube"])
#         legy4.SetTextAngle(0)
#         legy4.SetTextFont(42)
#         legy4.SetTextColor(color["IceCube"])
#         legy4.SetTextSize(0.020)
#         legy4.Draw("same")
    #Leg Dijet
        legy0  = TLatex(11,6.3e-39,"#splitline{"+text["PICASSO"]+"}{#it{arXiv:1611.01499}}")
        legy0.SetTextAngle(0)
        legy0.SetTextFont(42)
        legy0.SetTextColor(color["PICASSO"])
        legy0.SetTextSize(0.020)
        legy0.Draw("same")
        # Pico60 MET+X
        legy1  = TLatex(15,8e-41,"#splitline{"+text["Pico60"]+"}{#it{arXiv:1702.07666}}")
        legy1.SetTextAngle(0)
        legy1.SetTextFont(42)
        legy1.SetTextColor(color["Pico60"])
        legy1.SetTextSize(0.020)
        legy1.Draw("same")
    # SuperK MET+X
        legy2  = TLatex(10,6.0e-40,"#splitline{"+text["SuperKbb"]+"}{#it{arXiv:1503.04858}}")
        legy2.SetTextAngle(0)
        legy2.SetTextFont(42)
        legy2.SetTextColor(color["SuperKbb"])
        legy2.SetTextSize(0.020)
        legy2.Draw("same")
    # IceCube MET+X
        legy3  = TLatex(300,1.3e-39,"#splitline{"+text["IceCubebb"]+"}{#it{arXiv:1612.05949}}")
        legy3.SetTextAngle(0)
        legy3.SetTextFont(42)
        legy3.SetTextColor(color["IceCubebb"])
        legy3.SetTextSize(0.020)
        legy3.Draw("same")
        legy4  = TLatex(330,7.0e-41,"#splitline{"+text["IceCubett"]+"}{#it{arXiv:1601.00653}}")
        legy4.SetTextAngle(0)
        legy4.SetTextFont(42)
        legy4.SetTextColor(color["IceCubett"])
        legy4.SetTextSize(0.020)
        legy4.Draw("same")
    # SD dijet
        legx5  = TLatex(30,6.0e-42,"#splitline{#bf{CMS (dijet)}}{#splitline{Axial-vector mediator, Dirac DM}{g_{q} = 0.25, g_{DM} = 1.0}}")
        legx5.SetTextAngle(0)
        legx5.SetTextFont(42)
        legx5.SetTextColor(color["dijet"])
        legx5.SetTextSize(0.030)
        legx5.Draw("same")
#legend
#         legX=C.BuildLegend(0.55,0.12,0.95,0.40)#50 was 45
#         legX.SetBorderSize(0)
#         legX.SetFillStyle(0)
#         legX.SetTextFont(42)
#         legX.SetTextSize(0.015)
#         legX.Clear()
#         legX.SetHeader("#bf{Excluded 90% CL}")

# #         leg2.AddEntry(tgraph["dijet"],"#splitline{CMS dijet}{#it{[EXO-16-056]}}")
#         legX.AddEntry(tgraph["PICASSO"],"#splitline{"+text["PICASSO"]+"}{#it{[arXiv:1611.01499]}}")
#         legX.AddEntry(tgraph["Pico60"],"#splitline{"+text["Pico60"]+"}{#it{[arXiv:1702.07666]}}")
#         legX.AddEntry(tgraph["SuperKbb"],"#splitline{"+text["SuperKbb"]+"}{#it{[arXiv:1503.04858]}}")
#         legX.AddEntry(tgraph["IceCubebb"],"#splitline{"+text["IceCubebb"]+"}{#it{[arXiv:1612.05949]}}")
#         legX.AddEntry(tgraph["IceCubett"],"#splitline{"+text["IceCubett"]+"}{#it{[arXiv:1601.00653]}}")


#         legX.AddEntry(tgraph["dijet_2016"],"#splitline{Axial-vector med. Dirac DM}{g_{q} = 0.25, g_{DM} = 1.0}")
#         legX.Draw("same")

    elif DDresult=="SD":
                    # v Floor
        if vFloor == True :
            legy0  = TLatex(30,5.0e-45,"#nu Floor (permeable) arXiv/1506.08309")
            legy0.SetTextAngle(10)
            legy0.SetTextFont(42)
            legy0.SetTextColor(color["vFloor"])
            legy0.SetTextSize(0.025)
            legy0.Draw("same")
    # Pico2L MET+X
    # legy1  = TLatex(300,3.0e-39,text["Pico2L"])
    # legy1.SetTextAngle(15)
    # legy1.SetTextFont(42)
    # legy1.SetTextColor(color["Pico2L"])
    # legy1.SetTextSize(0.025)
    # legy1.Draw("same")
    # # Pico60 MET+X
    # legy2  = TLatex(300,6e-40,text["Pico60"])
    # legy2.SetTextAngle(15)
    # legy2.SetTextFont(42)
    # legy2.SetTextColor(color["Pico60"])
    # legy2.SetTextSize(0.025)
    # legy2.Draw("same")
    # # SuperK MET+X
    # legy3  = TLatex(250,1.5e-40,text["SuperK"])
    # legy3.SetTextAngle(5)
    # legy3.SetTextFont(42)
    # legy3.SetTextColor(color["SuperK"])
    # legy3.SetTextSize(0.025)
    # legy3.Draw("same")
    # # IceCube MET+X
    # legy4  = TLatex(415,1.07e-41,text["IceCube"])
    # legy4.SetTextAngle(14)
    # legy4.SetTextFont(42)
    # legy4.SetTextColor(color["IceCube"])
    # legy4.SetTextSize(0.025)
    # legy4.Draw("same")

        
        legy1  = TLatex(1.2,3e-38,"#scale[0.9]{#splitline{PICASSO}{arXiv:1611.01499}}")
        legy1.SetTextAngle(0)
        legy1.SetTextFont(42)
        legy1.SetTextColor(color["PICASSO"])
        legy1.SetTextSize(0.020)
        legy1.Draw("same")
        # Pico60 MET+X
        legy2  = TLatex(10,2e-40,"#splitline{Pico60}{arXiv:1702.07666}")
        legy2.SetTextAngle(0)
        legy2.SetTextFont(42)
        legy2.SetTextColor(color["Pico60"])
        legy2.SetTextSize(0.020)
        legy2.Draw("same")
    # SuperK MET+X
        legy3  = TLatex(7,2.5e-39,"#splitline{Super-K (b#bar{b})}{arXiv:1503.04858}")
        legy3.SetTextAngle(0)
        legy3.SetTextFont(42)
        legy3.SetTextColor(color["SuperKbb"])
        legy3.SetTextSize(0.020)
        legy3.Draw("same")
    # IceCube MET+X
        legy4  = TLatex(230,6e-39,"#splitline{IceCube (b#bar{b})}{arXiv:1612.05949}")
        legy4.SetTextAngle(0)
        legy4.SetTextFont(42)
        legy4.SetTextColor(color["IceCubebb"])
        legy4.SetTextSize(0.020)
        legy4.Draw("same")
        legy5  = TLatex(300,5.0e-41,"#splitline{IceCube (t#bar{t})}{arXiv:1601.00653}")
        legy5.SetTextAngle(0)
        legy5.SetTextFont(42)
        legy5.SetTextColor(color["IceCubett"])
        legy5.SetTextSize(0.020)
        legy5.Draw("same")

        legx6  = TLatex(1.2,2.5e-41,text["monoZ"])
        legx6.SetTextAngle(5)
        legx6.SetTextFont(42)
        legx6.SetTextColor(color["monoZ"])
        legx6.SetTextSize(0.020)
        legx6.Draw("same")
    # SD MET+X monophoton 
        legx7  = TLatex(30,2.0e-42,text["monophoton"])
        legx7.SetTextAngle(3)
        legx7.SetTextFont(42)
        legx7.SetTextColor(color["monophoton"])
        legx7.SetTextSize(0.020)
        legx7.Draw("same")
    # SD MET+X monojet
        legx8  = TLatex(30,2.0e-43,text["monojet"])
        legx8.SetTextAngle(2)
        legx8.SetTextFont(42)
        legx8.SetTextColor(color["monojet"])
        legx8.SetTextSize(0.020)
        legx8.Draw("same")
    # SD dijet
        legx9  = TLatex(1.22,4e-43,"CMS Dijet #it{[EXO-16-056]}")
        legx9.SetTextAngle(0)
        legx9.SetTextFont(42)
        legx9.SetTextColor(color["dijet"])
        legx9.SetTextSize(0.020)
        legx9.Draw("same")
    # SD trijet
        legx10  = TLatex(1.22,1.3e-39,"#splitline{CMS Boosted dijet}{#it{[EXO-16-030]}}")
        legx10.SetTextAngle(0)
        legx10.SetTextFont(42)
        legx10.SetTextColor(kAzure+1)
        legx10.SetTextSize(0.02)
        legx10.Draw("same")
    # Excluded at 90% CL
        legx11  = TLatex(5.3,4.0e-38,"Excluded at 90% CL")
        legx11.SetTextAngle(0)
        legx11.SetTextFont(42)
        legx11.SetTextColor(1)
        legx11.SetTextSize(0.025)
        legx11.Draw("same")

############
### Draw ###
############

#if not DijetOnly:
#    C.cd(2).SetPad(0.6,0.0,1.0,1.0)
#    C.Update()
#    C.cd(1)
#    leg.Draw("same")
#    C.Update()

if DDresult == "SI" and not DijetOnly:
    leg3=TLatex(mDM_lb,1.2e-35,"#bf{CMS} #it{Preliminary}")
    leg3.SetTextFont(42)
    leg3.SetTextSize(0.033)
    leg4=TLatex(36,1.2e-35,"13 fb^{-1} & 27 fb^{-1} & 36 fb^{-1} (13 TeV)")
    leg4.SetTextFont(42)
    leg4.SetTextSize(0.033)
elif DDresult == "SD" and not DijetOnly:
    leg3=TLatex(mDM_lb,1.2e-37,"#bf{CMS} #it{Preliminary}")
    leg3.SetTextFont(42)
    leg3.SetTextSize(0.033)
    leg4=TLatex(26,1.2e-37,"13 fb^{-1} & 27 fb^{-1} & 36 fb^{-1} (13 TeV)")
    leg4.SetTextFont(42)
    leg4.SetTextSize(0.033)
elif DDresult == "SI" and DijetOnly:
#    leg3=TLatex(600,2e-38,"#bf{CMS}")
    leg3=TLatex(mDM_lb,1.2e-37,"#bf{CMS} #it{Preliminary}")
    leg3.SetTextFont(42)
    leg3.SetTextSize(0.033)
#    leg4=TLatex(10,3e-36,"#splitline{#bf{Axial-vector med., Dirac DM}}{#it{g_{q} = 0.25, g_{DM} = 1}}")
    leg4=TLatex(70,1.2e-37,"27 fb^{-1} & 36 fb^{-1} (13 TeV)")
    leg4.SetTextFont(42)
    leg4.SetTextSize(0.033)
    leg5=TLatex(15,2.4e-38,"#scale[0.7]{Excluded at 90% CL}")
    leg5.SetTextFont(42)
    leg5.SetTextSize(0.033)
    leg5.Draw("same")  
elif DDresult == "SD" and DijetOnly:
#    leg3=TLatex(1.3,4e-38,"#scale[1]{#bf{CMS}}")
    leg3=TLatex(mDM_lb,1.2e-37,"#bf{CMS} #it{Preliminary}")
    leg3.SetTextFont(42)
    leg3.SetTextSize(0.033)
#    leg4=TLatex(10,3e-36,"#splitline{#bf{Axial-vector med., Dirac DM}}{#it{g_{q} = 0.25, g_{DM} = 1}}")
#    leg4=TLatex(180,1.2e-37,"36 fb^{-1} (13 TeV)")
    leg4=TLatex(70,1.2e-37,"27 fb^{-1} & 36 fb^{-1} (13 TeV)")
    leg4.SetTextFont(42)
    leg4.SetTextSize(0.033)
    leg5=TLatex(10,4e-38,"#scale[0.7]{Excluded at 90% CL}")
    leg5.SetTextFont(42)
    leg5.SetTextSize(0.033)
    leg5.Draw("same")

leg3.Draw("same")
leg4.Draw("same")

C.Update()

####################
### Draw RESULTS ###
####################

for analysis in analyses:
    tgraph[analysis].SetLineColor(color[analysis])
    tgraph[analysis].SetFillColor(color[analysis])
    tgraph[analysis].SetFillStyle(3003)
    tgraph[analysis].SetLineWidth( 102)
    tgraph[analysis].SetLineStyle(linestyle[analysis])
    tgraph[analysis].SetMarkerSize(0.1)
    tgraph[analysis].SetMarkerColor(color[analysis])
    if analysis=="dijet" or analysis == "dijet_2016" or analysis=="trijet":
        tgraph[analysis].SetLineWidth(2)
        tgraph[analysis].Draw("F,same")
        tgraph[analysis].Draw("same")
    elif analysis == "LUX" or analysis=="PandaX" or analysis=="CDMSlite" or analysis=="Cresst":
        tgraph[analysis].SetFillColor(kWhite)
        tgraph[analysis].Draw("same")
#    elif analysis == "Pico2L" or analysis=="Pico60" or analysis=="IceCube" or analysis=="SuperK":
    elif analysis == "PICASSO" or analysis=="Pico60" or analysis=="SuperKbb" or analysis=="IceCubebb" or analysis=="IceCubett":
        tgraph[analysis].SetFillColor(kWhite)
        tgraph[analysis].Draw("same")
    elif analysis == "monojet" or analysis=="monophoton" or analysis=="monoZ" or analysis=="dijet" or analysis=="dijet_2016":
        tgraph[analysis].Draw("same")
    elif analysis == "vFloor" :
        tgraph[analysis].SetLineWidth(-102)
        tgraph[analysis].Draw("same")

C.Update()

############
### Save ###
############

if DijetOnly : C.SaveAs(DDresult+"_CMSDD_Dijet.pdf")
elif METless : C.SaveAs(DDresult+"_CMSDD_Summary.pdf")
else         : C.SaveAs(DDresult+"_CMSDD_Summary_nodijet.pdf")

###########
### FIN ###
###########
