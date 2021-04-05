import numpy as np

dizi = np.array([1,2], ndmin=10) #ndim=32 ye kadar olabilir(max)
print(dizi)
print("dizi boyutu:",dizi.ndim)
print("bir dizi numpy de en fazla {} boyutlu olabilir".format(32))
