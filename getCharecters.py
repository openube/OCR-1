import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.filters.rank import median
from skimage.morphology import disk
def similar(val,minimum, maximum):
    if minimum<=val and maximum>=val:
        print True
        return True
    else:
        print False
        return False
#normal image
img = cv2.imread('Test Images/captcha.png')
#copys image
mask = img.copy()
#gets aspects of image
height, width, channels = img.shape
#grayscale image
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cut edges in image
edges = cv2.Canny(imgray,100,200)
#thresholds image
ret,thresh = cv2.threshold(imgray,150,255,cv2.THRESH_BINARY)
#creates kernal for dilation
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
#dilates image
dilated = cv2.dilate(thresh,kernel,iterations = 25)
#get contours
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
#draw contours on image
cv2.drawContours(imgray, contours, -1, (0,255,0), 3)
#create blank image
blank_image = np.zeros((height,width,3), np.uint8)
#counter
i = 0
#checking if filters result in too-few contours
x = 0
y = 0
passed = False
meme = 0
for cnt in contours:
    #gets bounding rect
    x,y,w,h = cv2.boundingRect(cnt)
    if h>300 and w>300:
        continue
    if h*4<w:
        continue
    if h<15 and w<15:
        continue
    if h<7 or w<7:
        continue
    i += 1
#check if length of countours is less than 10% of original length
if i<float(len(contours)*0.1):
    hMin = 0
    wMin = 0
else:
    hMin = 6
    wMin = 6
#looping and creating new image

for cnt in contours:
    i += 1
    if passed==True:
        prevX = x
        prevY = y
        prevH = h
        prevW = w
        meme = 1
    x,y,w,h = cv2.boundingRect(cnt)
    if meme == 1 and similar(x,float(prevX)*0.92, float(prevX)*1.08) and similar(y,float(prevY)*0.92, float(prevY)*1.08) and similar(h,float(prevH)*0.6, float(prevH)*1.4) and similar(w,float(prevW)*0.6, float(prevW)*1.4):
        if h>300 or w>300:
            continue
        if similar(w*h,float(width*height)*.5, float(width*height*1.5)):
            continue
        if h<hMin or w<wMin:
            continue
    else:
        if similar(w*h,float(width*height)*.5, float(width*height*1.5)):
            continue
       #discard large areas
        if h>300 or w>300:
            continue
        #discard long vertical lines
        if h*7<w:
        	continue
        #discard long horizontal lines
        if w*10<h:
            continue
        # discard areas that are too small
        if h<hMin or w<wMin:
            continue
    passed = True
    roi=mask[y:y+h,x:x+w]
    blank_image[y:y+h,x:x+w] = roi
    cv2.rectangle(img,(x,y),(x+w,y+h),(200,0,0),2)
cv2.imshow('ima', blank_image)
cv2.imshow('im', img)
cv2.waitKey(0)
# plt.subplot(131),plt.imshow(img, cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(132),plt.imshow(blur, cmap='gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(133),plt.imshow(imgray, cmap='gray')
# plt.title('Contoured Image'), plt.xticks([]), plt.yticks([])


# plt.show()
