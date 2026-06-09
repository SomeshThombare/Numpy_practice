import numpy as np

arr = np.array([10,20,40,50])
print(arr)

new_arr = np.append(arr,30)
print(new_arr)

dimentaion_2d = np.array([[1,2],[4,5]])
new = np.append(dimentaion_2d,[[3,6]],axis=0)
print(new)

"""arr1 = np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160]])
print(arr)

new_arr1 = np.append(arr1, [82,84,86,88],axis=0)
print(new_arr1)"""

dimentaion_2d = np.array([[1,2],[4,5]])
new = np.append(dimentaion_2d,[[3],[6]],axis=1)
print(new)
