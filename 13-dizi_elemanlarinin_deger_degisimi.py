import numpy as np
a = np.array(15)
b = np.array([1,2])
c = np.array([[3,4], [5,6]])
d = np.array([[[1,2,3,4,5],[6,7,8,9,10]],[[11,12,13,14,15],[16,17,18,19,20]]])

a = 20
b[1] = 20
c[1,0] = 20
d[1,0,2] = 20
print("A dizisini tek elemani: ",a)
print("B dizisinin 2. elemanı: ",b[1])
print("C dizisinin 2. elemanının 1. elemanı: ",c[1,0])
print("D dizisinin 2. elemanının 1. elemanı 3. elemanı: ",d[1,0,2])