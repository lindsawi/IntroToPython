#Lindsay Williams
#February 25, 2020
#Find the average of real and complex numbers less than 20

#long way has 4 lines
l= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20j,19j, 18j,17j, 16j, 15j, 14j, 13j, 12j, 11j, 10j, 9j,8j, 7j, 6j, 5j, 4j, 3j, 2j, 1j] 
for num in l:
    num2 = sum(l)/len(l)
print(num2)


#short way has 3 lines 
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20j,19j, 18j,17j, 16j, 15j, 14j, 13j, 12j, 11j, 10j, 9j,8j, 7j, 6j, 5j, 4j, 3j, 2j, 1j]
import numpy as np
print(np.mean(l))
