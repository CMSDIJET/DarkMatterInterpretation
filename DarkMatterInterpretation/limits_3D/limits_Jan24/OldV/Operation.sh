#!/bin/bash

DMmass=(1 50 100 150 200 250 300 350 400 450 500 550 600 650 700 750 800 850 900 950 1000 1050 1100 1150 1200 1250 1300 1350 1400)
Zmass=(500 1000 1500 1800 1850 1900 1950 2000 2050 2100 2150 2200 2250 2300 2350 2400 2450 2500 2550 2600 2650 2700 2750 2800 3000 3500 4000)

I_DM=0
Model=$1

if [ $Model == "V" ]; then
  for j in ${DMmass[@]};
  do
    I_Z=1
    FILENAME="limits_freq_qq_pfdijet2016_DMV_${j}GeV.C"
    Original="limits_freq_qq_pfdijet2016.C"
    cp $Original $FILENAME
    echo $FILENAME
    replace=${j}GeV
    sed -i '' 's/DMmass/'$replace'/g' $FILENAME
    for i in ${Zmass[@]};
    do
      line=$((I_DM*29+I_Z))
      Xsec=`python3.5 GetXsec_V.py $line`
      if [ $((I_Z)) -lt 10 ]; then
        replace1=Number0${I_Z}
      else
        replace1=Number${I_Z}
      fi
      sed -i '' 's/'$replace1'/'$Xsec'/g' $FILENAME
      I_Z=$((I_Z+1))
    done
    I_DM=$((I_DM+1))
  done
else
  for j in ${DMmass[@]};
  do
    I_Z=1
    FILENAME="limits_freq_qq_pfdijet2016_DMV_${j}.C"
    Original="limits_freq_qq_pfdijet2016.C"
    cp $Original $FILENAME
    echo $FILENAME
    replace=${j}GeV
    sed -i '' 's/DMmass/'$replace'/g' $FILENAME
    for i in ${Zmass[@]};
    do
      line=$((I_DM*29+I_Z))
      Xsec=`python3.5 GetXsec_AV.py $line`
      if [ $((I_Z)) -lt 10 ]; then
        replace1=Number0${I_Z}
      else
        replace1=Number${I_Z}
      fi
      sed -i '' 's/'$replace1'/'$Xsec'/g' $FILENAME
      I_Z=$((I_Z+1))
    done
    I_DM=$((I_DM+1))
  done

fi

