import numpy as np

dizi = np.array([1, 2, 3], dtype= "S")
print("dizi veri tipi:", dizi.dtype)

dizi = np.array(["123432432423", "2", "3"], dtype="U")
print("dizi veri tipi:", dizi.dtype)

dizi = np.array(["123432432423", "2", "3"], dtype="f")
print("dizi veri tipi:", dizi.dtype)