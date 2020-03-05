#Resriction Enzyme
#Lindsay Williams
#March 4, 2020
#Find Sequence lengths after restriction digestion

###################
#1. Write out the DNA sequence
#2. Define EcoRI Sequence
#3. Calculate sequence length of fragments
###################

###################
#1. Define sequence
mylist = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
print("Given this DNA sequence: ", "\n", mylist , "\n", "EcoRI would like to cut the sequence into 2 fragments...")
print("###################")

###################
#2. Define EcoRI sequence
EcoRI = "GAATTC"
print("EcoRI is a restriction enzyme that cuts at G*AATTC motifs.")
print("###################")

###################
#3. Calculate length of sequence fragments
frag1 = "TATCATACATATATATCGATGCGTTCAT"
firstt = frag1.count("T")
firsta = frag1.count("A")
firstc = frag1.count("C")
firstg = frag1.count("G")
first = frag1.count("T") + frag1.count("A") + frag1.count("C") + frag1.count("G")
print("The length of the first fragment is:", first)
print("###################")

frag2 = "ACTGATCGATTACGTATAGTA"
sec = frag2.count("ACTGATCGATTACGTATAGTA")
sect = frag2.count("T")
seca = frag2.count("A")
secc = frag2.count("C")
secg = frag2.count("G")
sec = frag2.count("T") + frag2.count("A") + frag2.count("C") + frag2.count("G")
print("The length of the second fragment is:", sec)
print("###################")

