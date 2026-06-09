import numpy as np

#additon to 2d and 3d arraay i.e 2D + 3D 

arr_2d = np.array([[1,2,3],
                   #[4,5,4],
                   [3,6,6]])

arr_3d = np.array([[[1,2,3],[3,4,4]],
                   [[5,6,2],[7,8,4]],
                   [[9,10,12],[11,12,13]]]) # 3D array

result = arr_2d + arr_3d
print(f"Addition of 2d and 3D array Result:\n{result}")

print("---------------------3x3------------------------------------")
arr_2d = np.array([[1,2,3],
                   [4,5,4],
                   [3,6,6]])

arr_3d = np.array([[[1,2,3],[3,4,4],[2,3,4]],
                   [[5,6,2],[7,8,4],[12,3,3]],
                   [[9,10,12],[11,12,13],[4,5,6]]]) # 3D array

result = arr_2d + arr_3d
print(f"Addition of 2d and 3D array Result:\n{result}")


#addition of 1d to 2d

arr_1d = np.array([1,2,3])

arr_2dd = np.array([[1,2,3],[3,4,5]])
result1d_2d = arr_1d + arr_2dd
print(f"Addition of 1d + 2d result:\n{result1d_2d}")

#addition of 1d to 3d
arr_1d = np.array([1,2,3])


arr_3d = np.array([[[1,2,3],[3,4,4],[2,3,4]],
                   [[5,6,2],[7,8,4],[12,3,3]],
                   [[9,10,12],[11,12,13],[4,5,6]]]) # 3D array

result1d_3d =  arr_1d + arr_3d 
print(f"addition of 1d + 3d result:\n{result1d_3d}")

#addition of 1d + 2d+ 3d
arr_1d = np.array([1,2,3])

arr_2d = np.array([[1,2,3],[3,4,5],[1,2,3]])

arr_3d = np.array([[[1,2,3],[3,4,4],[2,3,4]],
                   [[5,6,2],[7,8,4],[12,3,3]],
                   [[9,10,12],[11,12,13],[4,5,6]]]) # 3D array

result_1_2_3d = arr_1d + arr_2d + arr_3d
print(f"The addition of 1d + 2D + 3d:\n{result_1_2_3d}")