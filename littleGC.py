## Lindsay Williams
## LittleGC-421.py

## Write a script with a function that will calculate the GC content for a DNA sequence
## Create a random DNA sequence that is 5,000 bp long – STRING, no spaces, no commas
## Break the sequence into smaller sequences 100 bp long
## In a loop, use the GC function you created to calculate the GC content for each smaller sequence
## As a reminder, GC content is the G + C/total bp

## 1. 5000bp sequence
print("Here is the random sequence:")
import random
bases = ['A', 'T', 'G', 'C']
DNA = random.choices(bases, k=5000)
DNAseq = ''.join(DNA)
print(DNAseq)
print("#########################################")

## 2. Break the sequence - 100 bp long 
print("Here are the lists of 100 bp sequences:")
split_strings = []
n = 100
for index in range (0, len(DNAseq), n):
    split_strings.append(DNAseq[index : index + n]) 
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
