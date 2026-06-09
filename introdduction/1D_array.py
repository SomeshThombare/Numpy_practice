import numpy as np
#1D Array
ar_1d = np.array([1,2,3,4,5,6,7])
print(ar_1d)

#2D array
arr_2d = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print(arr_2d)


#3D or Multi dimentaion array
arr_3d = np.array([[[2,4,6],
                   [8,10,12],[13,34,45]]])
print(f"this is 3D array{arr_3d, arr_3d.ndim}D Array")


#creating array form pyhton listes
arr = np.array([1,2,3,4])
print(arr)

#with default value
#np.zeros(shape)

zeroes_arr = np.zeros(3)
zeroes_arr1 = np.zeros(5)
print(zeroes_arr, zeroes_arr1)
"""[0. 0. 0.] [0. 0. 0. 0. 0.]"""

#ones array
#rows and column (2 x 3)
print("2 x 3...")
ones_array = np.ones((2,3))
print(ones_array)

#rows and column (5 x 5)
ones_array = np.ones((5,5))
print(ones_array)
"""
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]"""


#full(shape, value)
#[[7 7]
# [7 7]]

filled_array = np.full((2,2),7)
print(filled_array)

filled_array = np.full((5,4),3)
print(filled_array)

#crating sequence of numbers in numpy
#arange()
#fumcton --> arange(start,stop,step)

arr = np.arange(2,21,2)
print(f"2 Table :{arr}")

#creating a identity matrix
#eye(size)
""" output
[[1. 0. 0. 0.]
 [0. 1. 0. 0.]
 [0. 0. 1. 0.]
 [0. 0. 0. 1.]]
 """

identity_matirx = np.eye(4)
print(identity_matirx)