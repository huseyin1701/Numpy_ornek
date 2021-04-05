import numpy as np

dizi = np.array([range(1, 13)]).reshape(1, 4, 3)
print(dizi)

for eleman in np.nditer(dizi,flags=["buffered"],op_dtypes=['S']):
    print(eleman)