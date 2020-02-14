# Counting bases
# Lindsay Williams 
# Feb 12, 2020

# import modules
# Add varaibles
# Ask for input
# Count bases
# print results

import random
dna = ["A","G","C","T"]
#initialise empty string
#this is where the bases will be added as they are generated
random_sequence=''
# We'll create a string of 100 random bases
for i in range(0,100):
    random_sequence+=random.choice(dna)
print(random_sequence)
## I had to figure out a different way to load a random dna sequence, the code in the powerpoint did not work for me

g_nuc = random_sequence.count("G")
string1 = "There are this many G's in the sequence: " + str(g_nuc) + " \n" 

a_nuc = random_sequence.count("A")
string2 = "There are this many A's in the sequence: " + str(a_nuc) + " \n" 

gc_nuc = random_sequence.count("C") + random_sequence.count("G") 
string3 = "There are this many G's and C's in the sequence: " + str(gc_nuc)  + "\n" 

print(string1+ string2 + string3)

##This works
