import cv2
from PIL import Image
img = cv2.imread('Test Images/signs.png');
vis = img.copy()
mser = cv2.MSER()
regions = mser.detect(img, None)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions]
img3 = Image.new("RGB", (1024, 1024), "White")
for x in hulls:
	min_x = 0
	max_x = 0
	min_y = 0
	max_y = 0
	min_x_coord = x[0][0][0]
	max_x_coord = x[0][0][0]
	min_y_coord = x[0][0][1]
	max_y_coord = x[0][0][1]
	for y in range (0,len(x)):
		if x[min_x][0][0] > x[y][0][0]:
			min_x = y
			min_x_coord = x[y][0][0]
		if x[min_y][0][1] > x[y][0][1]:
			min_y = y
			min_y_coord = x[y][0][1]
		if x[max_x][0][0] < x[y][0][0]:
			max_x = y
			max_x_coord = x[y][0][0]
		if x[max_y][0][1] < x[y][0][1]:
			max_y = y
			max_y_coord = x[y][0][1]
	box = (min_x_coord, min_y_coord, max_x_coord, max_y_coord)
	img2 = Image.open('Test Images/signs.png')
	w, h = img2.size
	img2 = img2.crop(box)
	w1, h1 = img2.size
	print float((w1*h1)/(w*h))
	if (float((w1*h1))/(w*h))<0.1:
		img3.paste(img2,box)
img3.show()	
cv2.polylines(vis, hulls, 1, (183, 255, 56))
cv2.imshow("img", vis)
cv2.waitKey(0)
cv2.destroyAllWindows()