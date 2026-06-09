import numpy as np

arr = np.array([1,2, np.nan, 4, np.nan, 6,7, np.nan])
#print(np.isnan(arr))
cleaned_arr = np.nan_to_num(arr)#defaut value is 0
cleaned_arr_1= np.nan_to_num(arr,nan=100)

print(cleaned_arr)
print(cleaned_arr_1)
