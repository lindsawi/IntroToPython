# Lindsay Williams
# April 9, 2020
# littlelists.py

## String -- “The quick brown fox jumped over the lazy dog”
## 1. Count the number of spaces in the above string. 
#For Loop
count = 0
line = "The quick brown fox jumped over the lazy dog"
for i in line: 
    if(i.isspace()):
        count=count+1
print("The number of blank spaces as determined by the for loop is: ", count)

#List Comprehension
mystring = 'The quick brown fox jumped over the lazy dog'
count = [s for s in mystring if s == ' ']
print("The number of blank spaces as determined by the list comprehension is: ", len(count))
print("############################")

## 2. Find all the words that have the letter “o” in the above string
#For loop
m = "o"
sen ="The quick brown fox jumped over the lazy dog"
text = sen.split(" ")
def string_m(m, sen): 
    string1 = []
    for word in text:
        if m in word:
            string1.append(word)
    return string1
print("The words that contain O as determined by for loop are: ", string_m(m, sen))
  
sen ="The quick brown fox jumped over the lazy dog"
string = []
text = sen.split(" ") #practicing 

#List Comprehension
name = [word for word in text if 'o' in (word)]
print("The words that contain O as determined by list comprehension are: ", name) #This works
print("############################") 


## 3. Find all the words that have at least 5 letters in the above string
#For Loop
k = 5
sen ="The quick brown fox jumped over the lazy dog"
def string_k(k, sen): 
    string = [] 
    text = sen.split(" ") 
    for x in text: 
        if len(x) >= k: 
            string.append(x) 
    return string 
print("The words longer than 5 letters as determined by the for loop is: ", string_k(k, sen))

sen ="The quick brown fox jumped over the lazy dog"
string = []
text = sen.split(" ")

#List Comprehension
name = [word for word in text if len(word) >= 5]
print("The words longer than 5 letters as determined by the list comprehension is: ", name)
print("############################")


#########################################
## 4. Find all the numbers from 1 to 1000 that have a “3” in it. Ex: 23, 37, 903
# For Loop
numbers = list(range(1001))
sub = str(3)
newlist = []
for i in numbers: 
    obj = str(i)
    if obj.count("3")>0:
        newlist.append(i)
print("These numbers contain the number 3 as determined by for loop are: ", newlist)


# List comprehension
listi = [num for num in range(1001)if str(num).count("3")>0] # list comprehensions are just definitions with functions
print("These numbers contain the number 3 as determined by list comprehension: ", listi)
