#filtering condition || like Boolean datatype true or false
import numpy as np

arr = np.array([10,20,30,40,50,60,70])
print(arr[arr>25]) #hw is return all greater value in array i.e;[30 40 50 60 70]
print(arr[arr<25])#[10 20]

print(arr>25) #he is retun in true or false i.e: [False False  True  True  True  True  True]



