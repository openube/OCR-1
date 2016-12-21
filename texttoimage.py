import struct
import scipy
import scipy.misc
import scipy.cluster
from PIL import Image
j = Image.open("j.png")
j.show()
j = j.convert("RGBA")
w, h = j.size
d = 0
tpix = w*h
c=0
print("Removing Background")
def almostEquals(a,b,thres=110):
    return all(abs(a[i]-b[i])<thres for i in range(len(a)))
for x in range(0, tpix): 
	if c==w:
		d=d+1
		c=0
	e,f,g,i = j.getpixel((c,d))
	if almostEquals((e,f,g), (255,255,255)):
		j.putpixel((c, d), (255, 255, 255,255))
		c=c+1
	else:
		j.putpixel((c,d),(0,0,0,0))
		c=c+1
j.show()
# c=0
# d=0
# for b in range(0,tpix):
# 	if c=w:
# 		d=d+1
# 		c=0
# 	e,f,g,i = j.getpixel((c,d))
# 	if e==0:
# 		