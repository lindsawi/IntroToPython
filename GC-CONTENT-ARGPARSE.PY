## GC-CONTENT-ARGPARSE.PY
## Lindsay Williams
## April 28, 2020

##1. Argparse the size of your random sequence
##2.Argparse the size of your smaller sequences
##3.Create a histogram for Gccontent *** new step ***

import math
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--SIZE", required=True, type = int, help = "Enter the size of your DNA sequence...")
ap.add_argument("-f", "--FRAGMENT", required = True, type = int, help = "Enter the size of fragment sequences...")
args = vars(ap.parse_args())

## 1. Random length sequence
print("Here is the random sequence:")
import random
bases = ['A', 'T', 'G', 'C']
DNA = random.choices(bases, k= (args["SIZE"]))
DNAseq = ''.join(DNA)
print("Here is the random sequence:" , DNAseq)

## 2. Break the sequence - randomly and save as list, argparse frag size
print("Here are the list of fragment sequences:")
split_strings = []
for index in range (0, args["SIZE"], args["FRAGMENT"]):
    split_strings.append(DNAseq[index : index +  args["FRAGMENT"]]) 
print(split_strings)
print("#########################################")

## 3. Loop - Calc GC content for smaller sequences
print("Here is the calculated GC content of each 100 bp sequence:")
def myGC(split_strings):	
        GCcount	=((split_strings.count("G")+split_strings.count("C"))/100)*100
        return(GCcount)	
        
GClist = [myGC(index) for index in split_strings] # calc for each sequence
print(GClist)
print("#########################################")

# 4. GC Content for Smaller Fragments Histogram
import numpy 
import matplotlib.pyplot as plt

content=plt.hist(GClist)
plt.title(" GC Content of Short Fragments")
plt.xlabel("GC Content")
plt.ylabel("Frequency")
plt.show()
