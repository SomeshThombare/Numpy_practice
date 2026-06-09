import numpy as np

matrix = np.array([[1,2,2],[2,3,4]])
vector = np.array([10,20,30])

result = matrix + vector
print(result)

"""[[11 22 32]
 [12 23 34]]"""


result = matrix * vector
print(result)
"""[[ 10  40  60]
 [ 20  60 120]]"""

#in this just change the variable names
arr1 = np.array([[1,2,2],[2,3,4]])
arr2 = np.array([10,20,30])

result = arr1 + arr2
print(result)