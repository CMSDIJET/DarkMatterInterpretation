from ROOT import *
import ast

#ADD METX

#def extrapolation( tgraph, DijetOnly, cmsanalyses, metless, mDM_lb ):
def extrapolation( tgraph, DijetOnly, metless, metx, mDM_lb ):

    DDgraph_extr = {}
    num_extr = 100

####################
## MET+X
#Step1 : Extrapolate from first non -100 point downto mDM_lb)
####################
    if not DijetOnly :
        for analysis in metx :
            print "Analysis ", analysis
            DDgraph_extr[analysis]=TGraph()
            #extrapolation based on the first point
            mDM_ref  = Double(0)  
            xsec_ref = Double(0)    
            tgraph[analysis].GetPoint(0,mDM_ref,xsec_ref); 
            mR_ref = 0.939*mDM_ref/(0.939+mDM_ref);
            for i in range(0, num_extr) :
                mDM_i = mDM_lb + i*(mDM_ref-mDM_lb)/num_extr
                mR_i = 0.939*mDM_i/(0.939+mDM_i);
                xsec_i = xsec_ref*(mR_i*mR_i)/(mR_ref*mR_ref)
                DDgraph_extr[analysis].SetPoint(i,mDM_i,xsec_i)     
                for i in range(0,tgraph[analysis].GetN()) :
                    mDM  = Double(0)
                    xsec  = Double(0)
                    tgraph[analysis].GetPoint(i,mDM,xsec)
                    DDgraph_extr[analysis].SetPoint(i+num_extr,mDM,xsec)        
                    
            tgraph[analysis] = DDgraph_extr[analysis]    
####################


####################
## Dijet,Trijet:
#[N.B: Step 1, 2a, 3 applies to Trijet] 
#Step1 : Extrapolate from first non -100 point downto mDM_lb)
#Step2 : 
  #a) copy input graphs into new one; 
  #b) extrapolate downward from i-1 to mDM_lb (N.B: MDM_i=-100 
  #c) extrapolate upward from i+1 to mDM_lb (N.B: MDM_i=-100)
#Step3 : Extrapolate from point N-1 downto mDM_lb 
#[N.B: discarding point N since it's equal to N-1]
####################


    #print "Dijet"



    index = 0 #keeps track of the index for filling graph
#    for analysis in cmsanalyses :
    for analysis in metless :
        index = 0 
        print "Analysis ", analysis
        DDgraph_extr[analysis]=TGraph()
#	tgraph[analysis]=TGraph()
#Tyler	tgraph[analysis]=TGraph("MonoZll/ScanMM/monoz_exo16038_sd.txt")

        #print "Step 1: Extrapolate from first non -100 point downto mDM_lb"

        #Step 1

        mDM_ref  = Double(0)  
        xsec_ref = Double(0)    
        tgraph[analysis].GetPoint(1,mDM_ref,xsec_ref) #0 => MDM = 100
#        print "mDM_ref ", mDM_ref, " xsec_ref ", xsec_ref
        mR_ref = 0.939*mDM_ref/(0.939+mDM_ref);
        for i_extr in range(0, num_extr) :
            mDM_i_extr = mDM_lb + i_extr*(mDM_ref-mDM_lb)/num_extr
            mR_i_extr = 0.939*mDM_i_extr/(0.939+mDM_i_extr);
            xsec_i_extr = xsec_ref*(mR_i_extr*mR_i_extr)/(mR_ref*mR_ref)
#            print "i = ", i_extr, " extrapolating with mDM_i = ", mDM_i_extr, "xsec_i = ", xsec_i_extr
            index = i_extr
#            print "index ", index
            DDgraph_extr[analysis].SetPoint(index,mDM_i_extr,xsec_i_extr)

        #Step2

        for i in range(1,tgraph[analysis].GetN()-2) : 
            mDM_i  = Double(0)
            xsec_i  = Double(0)
            mDM_im1  = Double(0)
            xsec_im1  = Double(0)
            mDM_ip1  = Double(0)
            xsec_ip1  = Double(0)
            tgraph[analysis].GetPoint(i,mDM_i,xsec_i)
            if i != 0 :
                tgraph[analysis].GetPoint(i-1,mDM_im1,xsec_im1)
            else :
                mDM_im1 = -999 
                xsec_im1 = -999 
            if i != tgraph[analysis].GetN()-1 :
                tgraph[analysis].GetPoint(i+1,mDM_ip1,xsec_ip1)
            else :
                mDM_ip1 = -999 
                xsec_ip1 = -999 

#            print "i ", i, "mDM_i,  mDM_i, mDM_ip1 ", mDM_i, mDM_i, mDM_ip1


            #copy input graphs
            if mDM_i != -100 :
                #print "Step 2a: Copy input graphs"                
                index = index + 1
                DDgraph_extr[analysis].SetPoint(index,mDM_i,xsec_i)        

            
            #extrapolation: 
            if mDM_i == -100 :
                #from previous point (i-1) down mDM_lb                
                if mDM_im1 !=-100 :
                    #print "Step 2b: Extrpolate downward from i-1 to mDM_lb"                
                    mDM_ref  = Double(0)
                    xsec_ref  = Double(0)
                    tgraph[analysis].GetPoint(i-1,mDM_ref,xsec_ref); 
                    mR_ref = 0.939*mDM_ref/(0.939+mDM_ref); 
                    for i_extr in range(0, num_extr+1) :
                        mDM_i_extr = mDM_lb + (num_extr-i_extr)*(mDM_ref-mDM_lb)/(num_extr)
                        mR_i_extr = 0.939*mDM_i_extr/(0.939+mDM_i_extr);
                        xsec_i_extr = xsec_ref*(mR_i_extr*mR_i_extr)/(mR_ref*mR_ref)
                        index = index + 1
                        DDgraph_extr[analysis].SetPoint(index,mDM_i_extr,xsec_i_extr)           

                #from subsequent point (i+1) up to mDM_lb                
                elif mDM_ip1 !=-100 :
                    #print "Step 2b: Extrpolate Upward from i+1 to mDM_lb"                            
                    mDM_ref  = Double(0)
                    xsec_ref  = Double(0)
                    tgraph[analysis].GetPoint(i+1,mDM_ref,xsec_ref);
                    mR_ref = 0.939*mDM_ref/(0.939+mDM_ref); 
                    for i_extr in range(0, num_extr) :
                        mDM_i_extr = mDM_lb + i_extr*(mDM_ref-mDM_lb)/(num_extr)
                        mR_i_extr = 0.939*mDM_i_extr/(0.939+mDM_i_extr);
                        xsec_i_extr = xsec_ref*(mR_i_extr*mR_i_extr)/(mR_ref*mR_ref)
                        index = index + 1
                        DDgraph_extr[analysis].SetPoint(index,mDM_i_extr,xsec_i_extr)           
                        


            
        tgraph[analysis] = DDgraph_extr[analysis]    


    #Step 3

#    for analysis in cmsanalyses :
    for analysis in metless :
        DDgraph_extr[analysis]=TGraph()
        #copy the graph up to N-3 included (lower xsec band)
        for i in range(0,tgraph[analysis].GetN()-2) :
            mDM  = Double(0)
            xsec  = Double(0)
            tgraph[analysis].GetPoint(i,mDM,xsec)
            DDgraph_extr[analysis].SetPoint(i,mDM,xsec)        
        #remove the last -100
        for i in range(tgraph[analysis].GetN()-2,tgraph[analysis].GetN()-1) :
            mDM  = Double(0)
            xsec  = Double(0)
            tgraph[analysis].GetPoint(i,mDM,xsec)
            DDgraph_extr[analysis].SetPoint(i,mDM,xsec)        

        extrafac = 5000

        mDM_ref  = Double(0)  
        xsec_ref = Double(0)    
        tgraph[analysis].GetPoint(tgraph[analysis].GetN()-2,mDM_ref,xsec_ref);
        mR_ref = 0.939*mDM_ref/(0.939+mDM_ref); #~ mn
        for i in range(0, num_extr*extrafac) :
            mDM_i = mDM_lb + (num_extr*extrafac-1-i)*(mDM_ref-mDM_lb)/(num_extr*extrafac)
            mR_i = 0.939*mDM_i/(0.939+mDM_i);
            xsec_i = xsec_ref*(mR_i*mR_i)/(mR_ref*mR_ref)
            DDgraph_extr[analysis].SetPoint(i+1+tgraph[analysis].GetN()-2,mDM_i,xsec_i)     

        tgraph[analysis] = DDgraph_extr[analysis]    

        # print "REPRINT GRAPH"
        # for i in range(0,tgraph[analysis].GetN()) :
        #     mDM  = Double(0)
        #     xsec  = Double(0)
        #     tgraph[analysis].GetPoint(i,mDM,xsec)
        #     print "REPRINT: mDM = ", mDM, "xsec = ", xsec


