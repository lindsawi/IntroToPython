## May 5, 2020
## Lindsay Williams

##1. Argparse to read in fasta file “dIul.fa” AND the taxon name “dIul”
##2. Determine how many records are in the file
##3. What is the shortest record? What is the longest record? 
##4. Run your GC function on each record sequence
##5. Plot a histogram of GC content (Hint: may need to save the results first)
##6. Which record has most GC content? Which record has least GC content?
##7. Translate each record
##8. Which record has most Stop codons? Which record has least Stop codons?

import math
import argparse
import pandas as pd

ap = argparse.ArgumentParser()
args = vars(ap.parse_args())

##2. Determine how many records are in the file
from Bio import SeqIO
import statistics

generator = SeqIO.parse("dIul.fa","fasta")
sizes = [len(rec) for rec in SeqIO.parse("dIul.fa", "fasta")]
amount = len(sizes)
print("There are this many records in the file: " , amount)

##3. What is the shortest record? What is the longest record?
big = []
for rec in SeqIO.parse("dIul.fa","fasta"):
        if len(rec) == 317079:
            big.append(rec.id)
print("Maximum length record(s):", big)

sm = [] 
for rec in SeqIO.parse("dIul.fa","fasta"):
        if len(rec) == 501:
            sm.append(rec.id)
print("Minimum length record(s):", sm)

##4. Run your GC function on each record sequence
GClist = [((item.seq.count("G"))+(item.seq.count("C"))/100*100) for item in SeqIO.parse("dIul.fa","fasta")]

##5. Plot a histogram of GC content (Hint: may need to save the results first)
import numpy 
import matplotlib.pyplot as plt

content=plt.hist(GClist)
plt.title(" GC Content of Short Fragments")
plt.xlabel("GC Content")
plt.ylabel("Frequency")
plt.show()
print("The GC Calculation is complete") 

##6. Which record has most GC content? Which record has least GC content?
high = []
for record in SeqIO.parse("dIul.fa","fasta"):
    if record.seq.count("G") + record.seq.count("C") == max(GClist):
        high.append(record.id)
print("This is the record with the highest GC content:", high)

low = []
for record in SeqIO.parse("dIul.fa","fasta"):
    if record.seq.count("G") + record.seq.count("C") == min(GClist):
        low.append(record.id)
print("This is the record with the lowest GC content:", low)

##7. Translate each record
late = [item.seq.translate() for item in SeqIO.parse("dIul.fa","fasta")]
print(late)

##8. Which record has most Stop codons? Which record has least Stop codons?
later = [item.seq.translate().count("*") for item in SeqIO.parse("dIul.fa","fasta")] #7514  and 0

most = []
for record in SeqIO.parse("dIul.fa","fasta"):
    if record.seq.translate().count("*") == max(later):
        most.append(record.id)

least = []
for record in SeqIO.parse("dIul.fa","fasta"):
    if record.seq.translate().count("*") == min(later):
        least.append(record.id)
print("This is the record with the most stop codons:", most)
print("These are the records with the least stop codons:", least)
