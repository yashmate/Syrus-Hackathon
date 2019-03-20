import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import webbrowser
def open_url(url):
    webbrowser.open(url)
img=cv2.imread('link.png')
decoded=pyzbar.decode(img)
print(decoded)
for data in decoded:
    print("DATA ", data.data)
    x=data.data
string=x.decode("utf-8")
print(string)
open_url(string)
cv2.imshow("IMAGE",img)
cv2.waitKey(0)
