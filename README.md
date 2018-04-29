# Download
```
cmsrel CMSSW_9_4_0 # (any version works)
cd CMSSW_9_4_0/src
cmsenv
git clone https://github.com/CMSDIJET/DarkMatterInterpretation.git 
```

# DarkMatterInterpretation

To plot coupling VS M_med, using 
```
python limits_gBdijetslimits_2017.py
```

To plot M_DM VS M_med VS coupling plot, using:
```
python limits_3D/dijet_For2017.py
```  
To plot M_DM VS M_med plot, using:
```
python PlotMM/plotMM.py
```
  
# comment
  the input of `PlotMM/plotMM.py` is in `PlotMM/Dijet/PlotMM/`, every time you run `limits_3D/dijet_For2017.py`, you will have an expected and observed text file for each model, you can copy that to `PlotMM/Dijet/PlotMM/`.
