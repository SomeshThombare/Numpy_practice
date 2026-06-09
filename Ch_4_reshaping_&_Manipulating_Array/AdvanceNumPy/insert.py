import numpy as np

arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr, 2, 25)
print(f"after inseration array{new_arr}")


