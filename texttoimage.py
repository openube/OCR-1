from PIL import Image
import scipy
import scipy.misc
import scipy.cluster
def removebg(clust):
	NUM_CLUSTERS = clust
	print 'reading image'
	im = Image.open('TestImages/sign.png')
	w, h = im.size
	if w*h>500000:
		w = w/2
		h = h/2
		im = im.resize((w,h))

	ar = scipy.misc.fromimage(im)
	shape = ar.shape
	ar = ar.reshape(scipy.product(shape[:2]), shape[2])

	print 'finding clusters'
	codes, dist = scipy.cluster.vq.kmeans(ar.astype(float), NUM_CLUSTERS)
	print 'cluster centres:\n', codes

	vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
	counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

	index_max = scipy.argmax(counts)                    # find most frequent
	peak = codes[index_max]
	j = im
	j.show()
	j = j.convert("RGBA")
	d = 0
	tpix = w*h
	c=0
	p = 0
	pix_val = list(j.getdata())
	print("Removing Background")
	def almostEquals(a,b,thres=110):
	    return all(abs(a[i]-b[i])<thres for i in range(len(a)))
	if clust == 2:
		for x in range(0, tpix): 
			if c==w:
				d=d+1
				c=0
			e,f,g,i = j.getpixel((c,d))
			if almostEquals((e,f,g), (codes[0][0], codes[0][1], codes[0][2])) or almostEquals((e,f,g), (codes[1][0], codes[1][1], codes[1][2])):
				j.putpixel((c, d), (255, 255, 255, 255))
				c=c+1
			else:
				j.putpixel((c,d),(0,0,0,0))
				c=c+1
				p=p+1
	if clust==1:
		for x in range(0, tpix): 
			if c==w:
				d=d+1
				c=0
			e,f,g,i = j.getpixel((c,d))
			if almostEquals((e,f,g), (peak[0], peak[1], peak[2])):
				j.putpixel((c, d), (255, 255, 255, 255))
				c=c+1
			else:
				j.putpixel((c,d),(0,0,0,0))
				c=c+1
				p=p+1
	print p
	print tpix
	j.show()
	if clust==2 and p<(tpix/10) and p<(tpix/1.5):
		removebg(1)
removebg(2)



#Notes
#If doesn't have a pixel of very similar color directly next to it, remove
#possible add up values of the rgb, then put into matrix
