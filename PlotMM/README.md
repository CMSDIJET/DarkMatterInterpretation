Welcome to the CMS EXO MET+X Combination repository

This project contains the scripts for the 2016 MET+X combination/summary plots, and corresponding files.

In particular, for each analysis, the directories are:
- Cards: Data cards (in the CMS Combine format) and corresponding root files 
- ScanMg: Scan of the (M,g) plane (root curve)
- ScanMM: Scans of the (M,M) plane, most commonly used so far (TGraphs or text files)

The main plotting scripts are:
- plotMM.py (curves in MM plane)
- plotMx.py (curves in DD plane)
- plotScalar.py (1D S/P plots)

Parameters to be adjusted
- Mediator type (V/A/S/P)
- With or w.o. dijet analyses

PLEASE provide your results for Summary plots
- Either as a text file (example: mono-Z)
- Or as a TGraph in a root file (example: trijet)
- But please don't provide it as a script, as this is not practical & error prone

Happy Combining

 --- The CMS EXO MET+X Combination WG