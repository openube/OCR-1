from PIL import Image
import sys
sys.setrecursionlimit(100000)
o = 0
def getConnections(Arr):
	global o
	tpix = len(Arr)
	imArray = Arr
	fullList = imArray
	groups = []
	print len(imArray)
	def inProximity(Pix, Arr):
		global o
		groupCoords = []
		groupCoords.append(Pix)
		Arr.remove(Arr[1])
		tgroup = []
		def loop(groupCoords):
			global o
			new = []
			for x in range (0,len(groupCoords)):
				global o
				xCoord = groupCoords[x][0]
				yCoord = groupCoords[x][1]
				if [xCoord, yCoord+1] in Arr:
					tgroup.append([xCoord,yCoord+1])
					new.append([xCoord,yCoord+1])
					Arr.remove([xCoord,yCoord+1])

				if [xCoord, yCoord-1] in Arr:
					tgroup.append([xCoord,yCoord-1])
					new.append([xCoord,yCoord-1])
					Arr.remove([xCoord,yCoord-1])

				if [xCoord+1, yCoord] in Arr:
					tgroup.append([xCoord+1,yCoord])
					new.append([xCoord+1,yCoord])
					Arr.remove([xCoord+1,yCoord])
				if [xCoord+1,yCoord+1] in Arr:
					tgroup.append([xCoord+1,yCoord+1])
					new.append([xCoord+1,yCoord+1])
					Arr.remove([xCoord+1,yCoord+1])
				
				if [xCoord+1,yCoord-1] in Arr:
					tgroup.append([xCoord+1,yCoord-1])
					new.append([xCoord+1,yCoord-1])
					Arr.remove([xCoord+1,yCoord-1])
				
				if [xCoord-1,yCoord] in Arr:
					tgroup.append([xCoord-1,yCoord])
					new.append([xCoord-1,yCoord])
					Arr.remove([xCoord-1,yCoord])

				if [xCoord-1, yCoord+1] in Arr:
					tgroup.append([xCoord-1,yCoord+1])
					new.append([xCoord-1,yCoord+1])
					Arr.remove([xCoord-1,yCoord+1])

				if [xCoord-1, yCoord-1] in Arr:
					tgroup.append([xCoord-1,yCoord-1])
					new.append([xCoord-1,yCoord-1])
					Arr.remove([xCoord-1,yCoord-1])
				o = o+1
				print o

			if len(new)>0:	
				loop(new)
			elif len(Arr)>1:
				groups.append(tgroup)
				inProximity(Arr[1], Arr)
				#im.show()
			else:
				return
		if len(Arr)<20:
			l = Image.new("RGB", (1024, 1024), "White")
			for x in range (0, len(groups)):
				if len(groups[x])<(tpix/4) and len(groups[x])>(tpix/1500):
					for y in range (0, len(groups[x])):
						l.putpixel((groups[x][y][0],groups[x][y][1]),(0,0,0,0))
			l.show()


			return
		else:
			print len(Arr)
			loop(groupCoords)

	def groupSearch(Arr):
		inProximity(Arr[1], Arr)







	# def groupSearch(Arr):
	# 	groupCoords = []
	# 	xCoord = Arr[1][0]
	# 	yCoord = Arr[1][1]
	# 	Arr.remove(Arr[1])
	# 	if [xCoord, yCoord+1] in Arr:
	# 		groupCoords.append([xCoord,yCoord+1])
	# 		groupCoords.append([xCoord,yCoord])
	# 		Arr.remove([xCoord,yCoord+1])
	# 		gc.append([xCoord,yCoord])
	# 		groupSearch(Arr)

	# 	if [xCoord, yCoord-1] in Arr:
	# 		groupCoords.append([xCoord,yCoord-1])
	# 		Arr.remove([xCoord,yCoord-1])
	# 		groupSearch(Arr)

	# 	if [xCoord+1, yCoord] in Arr:
	# 		groupCoords.append([xCoord+1,yCoord])
	# 		Arr.remove([xCoord+1,yCoord])
	# 		groupSearch(Arr)
		
	# 	if [xCoord+1,yCoord+1] in Arr:
	# 		groupCoords.append([xCoord+1,yCoord+1])
	# 		Arr.remove([xCoord+1,yCoord+1])
	# 		groupSearch(Arr)
		
	# 	if [xCoord+1,yCoord-1] in Arr:
	# 		groupCoords.append([xCoord+1,yCoord-1])
	# 		Arr.remove([xCoord+1,yCoord-1])
	# 		groupSearch(Arr)
		
	# 	if [xCoord-1,yCoord] in Arr:
	# 		groupCoords.append([xCoord-1,yCoord])
	# 		Arr.remove([xCoord-1,yCoord])
	# 		groupSearch(Arr)

	# 	if [xCoord-1, yCoord+1] in Arr:
	# 		groupCoords.append([xCoord-1,yCoord+1])
	# 		Arr.remove([xCoord-1,yCoord+1])
	# 		groupSearch(Arr)

	# 	if [xCoord-1, yCoord-1] in Arr:
	# 		groupCoords.append([xCoord-1,yCoord-1])
	# 		Arr.remove([xCoord-1,yCoord-1])
	# 		groupSearch(Arr)

	# 	return Arr
	groupSearch(imArray)
