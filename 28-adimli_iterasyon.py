import numpy as np

dizi = np.array([range(1, 13)]).reshape(4, 3)
print(dizi)

for eleman in np.nditer(dizi[:, 1]):
    print(eleman)

for eleman in np.nditer(dizi[1:2, :]):
    print(eleman)