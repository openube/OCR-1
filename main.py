import cv2
from fetchConnections import fetchConnections

from removeBackground import removeBackground

fetchConnections(removeBackground(2))



#Notes
#If doesn't have a pixel of very similar color directly next to it, remove
#possible add up values of the rgb, then put into matrix
