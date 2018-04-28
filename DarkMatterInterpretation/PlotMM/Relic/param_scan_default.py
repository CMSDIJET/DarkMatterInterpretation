#! /usr/bin/env python

#import numpy as np
import fileinput
import sys
import os
import pickle

#Set the proper paths 
maddm_path = os.path.split(os.path.dirname(os.path.realpath( __file__ )))[0]
pieces = maddm_path.split('/')
maddm_path = maddm_path.replace(pieces[-1], '')
sys.path.append(maddm_path)

from init import *
from darkmatter import *

#Read in the DM information

with open('dm_object.pik', 'r') as f:
	dm = pickle.load(f)

os.chdir(maddm_path)

#Print out some basic information about the dark matter particle.
print "--------------------------------------------"
print "Model: "+dm._modelname
print "Project Name: "+dm._projectname
print "Parameter Card: "+dm._paramcard
print "DM particles: "+dm._dm_particles[0].get('name')
print "DM spin: "+str(dm._dm_particles[0].get('spin'))
print "--------------------------------------------"


Mmed_list = [350,2200,2000,1800,1600,1400,1200,1000,800,700,600,550,500,450,400]#,200]
MDM_list = [100,150,160,170,180,190,200,250,300,350,400,450,500,550,600,650,700,750]
#0
#Mmed_list  = [1000,900,800,700,600,500,400,300,200,100]#zoomscan
#MDM_list = [100,150,200,250,300,350,400,450,500]#zoomscan
#1
#Mmed_list  = [3000,2000,1000,750,500,300,200,100]#largescan
#MDM_list = [100,200,300,400,500,750,1000]#largescan
#2
#Mmed_list  = [400,500,600,700,800]
#MDM_list = [150,155,160,165,170,175,180,185,190,195,200]
#3
#Mmed_list  = [400,500,600,700,800,1000,1200,1400,1600,1800,2000,2500,3000,5000,10000,50000,100000]
#MDM_list  = [150,155,160,165,170,175,180,185,190,195,200]

outputfile = open("/afs/cern.ch/work/c/croskas/MG5_aMC_v2_2_3/maddm_v1.0/outputMadDM.dat", "w") #"<-----Change here ----!!!"
	
for Mmed in Mmed_list:
	for MDM in MDM_list: 
                #Change the parameter with name 'MPS' in the param_card.dat to the value MA
		dm.ChangeParameter('Mphi',  Mmed)#MZp #MS
		#Change the parameter with name 'MnH1' in the param_card.dat to the value MDM
		dm.ChangeParameter('Mchi', MDM) #MnH1
		
		if True:
         		#Calculate relic density
			omega = dm.CalculateRelicAbundance()
		        #Output the results on the screen and in the output file
			printstring = "M(med) = "+str(Mmed)+" & M(DM) = "+str(MDM)+" ==> Omega*h^2 = "+str(omega) 
			print printstring
			outputstring = str(Mmed)+" "+str(MDM)+" "+str(omega)+" \n"
			outputfile.write(outputstring)
							
outputfile.close()





#Change the directory to MadDM root folder so that code can run properly.




#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#CHANGE THIS PART FOR YOUR PARAMETER SCAN
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#Add as many for loops as you wish to scan over parameters
#NOTE:  The default script varies over two parameters (param1 and param2), and outputs the
#		results in the format "param1    param2    omegah^2" on the screen and in the output file.
#		Please make sure to change the number of "for" loops, calls to ChangeParameter() and the
#		output commands to account for the number of parameters you wish to vary. The critical
#		places where changes are usually required are marked with "<-----Change here ----!!!"


#bound = ['lowbound','fullbound']

#Define the arrays of values your parameters should take.
#If you are using np.arrange, the format is np.arange(init_val, final_val, step_size)
#param1_values = np.arange(0.001, 0.501, 0.01) #"<-----Change here ----!!!"
#param2_values = np.arange(0.001, 0.501, 0.01) #"<-----Change here ----!!!"

#EXO-12-055 compatibel



#Mmed_list = [350,2200,2000,1800,1600,1400,1200,1000,800,700,600,550,500,450,400]#,200]
#MDM_list = [100,150,160,170,180,190,200,250,300,350,400,450,500,550,600,650,700,750]
#0
#Mmed_list  = [1000,900,800,700,600,500,400,300,200,100]#zoomscan
#MDM_list = [100,150,200,250,300,350,400,450,500]#zoomscan
#1
#Mmed_list  = [3000,2000,1000,750,500,300,200,100]#largescan
#MDM_list = [100,200,300,400,500,750,1000]#largescan
#2
#Mmed_list  = [400,500,600,700,800]
#MDM_list = [150,155,160,165,170,175,180,185,190,195,200]
#3
#Mmed_list  = [400,500,600,700,800,1000,1200,1400,1600,1800,2000,2500,3000,5000,10000,50000,100000]
#MDM_list  = [150,155,160,165,170,175,180,185,190,195,200]

#outputfile = open("/afs/cern.ch/work/c/croskas/MG5_aMC_v2_2_3/maddm_v1.0/outputMadDM.dat", "w") #"<-----Change here ----!!!"
	
#for Mmed in Mmed_list:
#	for MDM in MDM_list: 
                #Change the parameter with name 'MPS' in the param_card.dat to the value MA
#		dm.ChangeParameter('Mphi',  Mmed)#MZp #MS
#		#Change the parameter with name 'MnH1' in the param_card.dat to the value MDM
#		dm.ChangeParameter('Mchi', MDM) #MnH1
		
#		if True:
  ###       		#Calculate relic density
##			omega = dm.CalculateRelicAbundance()
#		        #Output the results on the screen and in the output file
##			printstring = "M(med) = "+str(Mmed)+" & M(DM) = "+str(MDM)+" ==> Omega*h^2 = "+str(omega) 
#			print printstring
#			outputstring = str(Mmed)+" "+str(MDM)+" "+str(omega)+" \n"
#			outputfile.write(outputstring)
			
#outputfile.close()
#---------------------------------------------------------------------------
#-------------------------------------------------------------------------
