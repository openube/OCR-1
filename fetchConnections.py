from PIL import Image
import numpy as np
from scipy.spatial.distance import cdist
import sys

sys.setrecursionlimit(100000)

groups = []

def finishImage(groupList):

	newL = []
	groupSizeCounter = 0

	for x in range (0,len(groupList)):

		groupSizeCounter = groupSizeCounter + len(groupList[x])
		averageGroupSize = groupSizeCounter/float(len(groupList))

	for groupNumber in range (0,len(groups)):

		if ((len(groupList[groupNumber]))/float(averageGroupSize)) < 8 and ((len(groupList[groupNumber]))/float(averageGroupSize)) > 0.3:
			newL.append(groupList[groupNumber])

	l = Image.new("RGB", (1024, 1024), "White")

	for x in range (0, len(newL)):	

		for y in range (0, len(newL[x])):

			l.putpixel((newL[x][y][0],newL[x][y][1]),(0,0,0,0))

	sys.exit(0)

def fetchConnections(Arr):

	global extractedArr
	extractedArr = np.array(Arr)

	if len(extractedArr)==0:

		finishImage(groups)
		return

	groupList = []
	groupCoords = [extractedArr[0]]

	def out(groupCoords):

		global extractedArr
		nextTo = extractedArr[(cdist(extractedArr,groupCoords)<1.5).any(1)]

		for x in range(nextTo.shape[0]):

			groupList.append(nextTo[x])
			index = np.argwhere((extractedArr == nextTo[x]).all(1))
			extractedArr = np.delete(extractedArr, (index), axis=0)

		if len(nextTo)==0:

			groups.append(groupList)
			fetchConnections(extractedArr)

		out(nextTo)

	out(groupCoords)
		