import numpy as np
#addition os 3D array i.e 3D + 3D

arr_3d = np.array([[[1,2],[3,4]],
                   [[5,6],[7,8]],
                   [[9,10],[11,12]]]) # 3D array

Arr_3d = np.array([[[1,2],[3,4]],
                   [[11,12],[23,45]],
                    [[34,54],[23,43]]]) 

result_3d = arr_3d + Arr_3d
print(f"Addition of 3D arrya reult:{result_3d}")

