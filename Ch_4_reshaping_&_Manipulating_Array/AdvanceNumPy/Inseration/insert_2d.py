import numpy as np

arr = np.array([[10,20],[40,50]])
print(arr)

#new_arr_2d = np.insert(arr, 1,[35,36,37],axis=None)
new_arr_2d = np.insert(arr, 1,[35,36],axis=1)
#new_arr_2d = np.insert(arr, 1,[35,36,37],axis=1)

print(new_arr_2d)

"""output:
[[10 20 30]
 [35 36 37] <--
 [40 50 60]]"""

print("___________________________________________")

arr = np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120],[130,140,150,160]])
print(arr)

new_arr = np.insert(arr, 2,[82,84,86,88],axis=1)
print(new_arr)


