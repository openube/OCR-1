import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.filters.rank import median
from skimage.morphology import disk

#normal image
img = cv2.imread('Test Images/sshot.png')
#grayscale image
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cut edges in image
edges = cv2.Canny(imgray,100,200)
#blur then filter
#blur = cv2.GaussianBlur(edges,(5,5),0)
#remove noisey pixels
#removeNoise = median(blur, disk(10))
#threshold image
ret,thresh = cv2.threshold(edges,150,255,cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
print kernel
dilated = cv2.dilate(thresh,kernel,iterations = 2) # dilate
#get contours
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

cv2.drawContours(imgray, contours, -1, (0,255,0), 3)

idx =0 
for cnt in contours:
    idx += 1
    x,y,w,h = cv2.boundingRect(cnt)
    if h>300 and w>300:
        continue
    if h*4<w:
    	continue
    # discard areas that are too small
    if h<10 and w<10:
        continue
    if h<7 or w<7:
    	continue
    roi=img[y:y+h,x:x+w]
    cv2.rectangle(img,(x,y),(x+w,y+h),(200,0,0),2)
cv2.imshow('im', img)
cv2.waitKey(0)
# plt.subplot(131),plt.imshow(img, cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(132),plt.imshow(removeNoise, cmap='gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(133),plt.imshow(imgray, cmap='gray')
# plt.title('Contoured Image'), plt.xticks([]), plt.yticks([])


# plt.show()