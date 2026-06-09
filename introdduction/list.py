#without numpy
tempreature = [32.5,31.3,34.5,56.6,43.4]
total = 0
for temp in tempreature:
    total += temp

average = total/len(tempreature)
print(average)

#using numpy
import numpy as np
tempreature = np.array([32.5,31.3,34.5,56.6,43.4])
avg = np.mean(tempreature)
print(avg)

min = np.min(tempreature)
print(f"The minimum no is :{min}")


max = np.max(tempreature)
print(F"The maximun no is :{max}")


# difference betweeen list and Numpy
python_list = [1,2,3,4,5]
print(python_list)

numpy_array = np.array([1,2,3,4,5])
print(numpy_array)