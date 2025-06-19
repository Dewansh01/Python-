import numpy as np
import time 

size = 10000

list1 = list(range(size))
list2 = list(range(size))

arr1 = np.array(range(size))
arr2 = np.array(range(size))

t1 = time.time()
resultlist = [(a*b) for a,b in zip(list1,list2)]
print("time taken to complete calculation in list ", time.time() - t1)

t2 = time.time()
resultarr = arr1*arr2
print("time taken to complete calculation in array ", time.time() - t2)
