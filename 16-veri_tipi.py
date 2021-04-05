import numpy as np

dizi = np.array([1, 2, 3])
print("dizi veri tipi:", dizi.dtype)

dizi = np.array(["1", "2", "3"])
print("dizi veri tipi:", dizi.dtype) #U1 bir elemanlı

dizi = np.array(["11", "222", "3333"])
print("dizi veri tipi:", dizi.dtype) # U4 en uzun eleman 4 elemanlı

dizi = np.array([14354534534534534543, 2, 3])
print("dizi veri tipi:", dizi.dtype)

dizi = np.array([1435453453453455252353553234543, 2, 3])
print("dizi veri tipi:", dizi.dtype)