#file>settings>project>Python interpreter----> arama kısmına opencv-python yaz ve indir
#resim diye bir klasör açıp içine resim koy.Onun da yolunu belirtip dizi şeklinde değerleri yazdırırız.
import numpy  #kullanmadığımız için silik  yazılı
import cv2
resim = cv2.imread("resim/a.jpg")
print(resim)
print(type(resim)) #<class 'numpy.ndarray'> çıktısı

cv2.imshow("asd",resim)
cv2.waitKey(0)