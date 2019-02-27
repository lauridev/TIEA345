from matplotlib import pyplot as plt
import numpy as np
import cv2

#avataan kuvat
img1=cv2.imread("kuva3.jpg",0)
img2=cv2.imread("kuva4.jpg",0)
orb = cv2.ORB_create()
#kp = orb.detect(img,None)
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
#img2 = cv2.drawKeypoints(img,kp,None,color=(0,255,0),flags=0)

bf =cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches =bf.match(des1,des2)

#Jarjestaa yhtenevaisyydet yhdistavien pisteiden avulla
matches =sorted(matches, key =lambda x:x.distance)

#Piirtaa kuvan jossa nakyy kahdeksan parasta yhtenevaisyytta
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:8],None,flags =2)
#Tallentaa kuvan
plt.imshow(img3),plt.savefig("tulos.png")
