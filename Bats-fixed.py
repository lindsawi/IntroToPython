# Bats-fixed.py 
# Rewrite bat names
# Lindsay Williams 
# March 27, 2020

# import modules
# Add varaibles
# Ask for input
# Calculate population estimation
# print results

species1_input = input("What is the name of species 1? " )
##NAME = ("Myotis austroriparius")
##print(species1_input)
species2_input = input("What is the name of species 2? " )
##print(species2_input)
##NAME2 = ("Myotis septentrionalis")
species3_input = input("What is the name of species 3? " )
##NAME3 = {"Eptesicus fuscus"}
##print(species3_input)

species_1 = str.upper(species1_input)
species_2 = str.upper(species2_input) 
species_3 = str.upper(species3_input) 


string1 = species_1[0:3] + species_1[7:10] + " \n" 
string2 = species_2[0:3] + species_2[7:10]  + " \n" 
string3 = species_3[0:3] + species_3[10:13] + " \n" 

new_statement = "There are three species of bats: " + "\n" +  string1 +  string2 + string3
print(new_statement) 
