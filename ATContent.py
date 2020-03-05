#AT Content
#Lindsay Williams
#February 26, 2020
#Find percent content AT

###################
#1. Write out the DNA sequence
#2. Find AT content of sequence
#3. Print AT percent content
###################

###################
#1. Define sequence
mylist = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
print(" Given this DNA sequence: ", "\n ", mylist , "\n", "what is the AT content?")
print("###################")


###################
#2. Find AT content of the sequence
total = len(mylist)
a_nuc = mylist.count("A")
string1 = "There are this many A's in the sequence: " + str(a_nuc) + " \n" 
print(string1)
print("###################")

t_nuc = mylist.count("T")
string2 = "There are this many T's in the sequence: " + str(t_nuc) + " \n" 
print(string2)
print("###################")

at_nuc = mylist.count("A") + mylist.count("T") 
string3 = "There are this many A's and T's in the sequence: " + str(at_nuc)  + "\n" 
print(string3)
print("###################")

###################
#3. Find AT percent content of the sequence
percent = at_nuc/total* 100
print("This is the AT percent content: ", percent)
print("###################")

# IT WORKS! Had trouble not counting sequence as 0 due to [] after "" for mylist. 
