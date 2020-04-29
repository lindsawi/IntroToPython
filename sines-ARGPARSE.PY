## sines-ARGPARSE.PY
## Lindsay Williams
## April 28, 2020

##1. Argparse reading in the aVan bedfile
##2.Argparse retaining the SINE family
##3. Argparse the genome size (390758124) *** new step ***
##4.Create new column “Proportion” which is Length/genome size ***new step ***
##5.Save the SINEs dataframe as “aVan.csv” *** new step***

import math
import argparse
import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("-b", "--BEDFILE", required=True, help = "Please enter the name of your bedfile")
ap.add_argument("-n", "--FAMILY", required=True, help = "Enter the family you want to retain")
ap.add_argument("-g", "--GENOMESIZE", required=True, type = int, help = "Enter the size of genome (bp)")
args = vars(ap.parse_args())

## 1. Assign column names
fields = ["Scaffold", "Start", "Stop", "Element", "Score", "Strand", "Family", "Sub-Family", "Divergence"]
bed = pd.read_csv ("aVan_rm.bed", names = fields, sep ="\t")
print(bed.head())


## 2. Families in sample
family = bed.Family.unique()
print ("The unique families in the file are ", family)

## 4.  Create new dataframe from that file using unique elements in family SINE
new = bed.loc[bed["Family"] == args["FAMILY"]]   
print("Here is the new dataframe: " , new)

## 5.  Drop columns Strand and Score  
newcol = new.drop(["Strand", "Score"], axis = 1)
print(newcol.head())

## 6. Create new column Length
newcol['Length'] = newcol['Stop'] - newcol['Start']
print("New column length has been created...")

## 7. Determine min, max, and mean for all SINEs
min = newcol["Length"].min()
print("The minimum value for SINEs is ",min) 
max = newcol["Length"].max()
print("The maximum value for SINEs is ",max)
mean = newcol["Length"].mean()
print("The mean value for SINEs is ",mean)

## 8. Determine min, max, and mean length for each sub-family of SINE (metulj and ZenoSINE)
sf_min = newcol.groupby("Sub-Family")["Length"].min()
print ("Minimum values of the sub-families are ", "\n", str(sf_min))
sf_max = newcol.groupby("Sub-Family")["Length"].max()
print ("Maximum values of the sub-families are ", "\n", str(sf_max))
sf_mean= newcol.groupby("Sub-Family")["Length"].mean()
print("Mean values of the sub-families are ", "\n",  str(sf_mean))

##9. Proportion column
newcol['Proportion'] = newcol['Length']/args['GENOMESIZE']

## 10. NEW dataframe
newcol.to_csv("aVan.csv")
