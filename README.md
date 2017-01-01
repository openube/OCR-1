# OCR

Requirements:
- Python
- Scipy
- PIL Imaging Library

To Do List:
- [x] Remove background of Image
- [x] Find Strands of Possible Charecters
- [x] Remove Strands of Pixels which are most likely not charecters
- [x] Improve Connected-component labeling algorithm
- [x] Incorperate Numpy Arrays in fetchConnections to increase speed
- [x] Clean up fetchConnections to eliminate ongoing recursive function
- [ ] Improve the removal of meaningless objects
- [x] Speed up process (Currently takes upwards of 20s to do small images)
- [ ] Begin matching groups of pixels to their corresponding charecters
- [ ] Format the text after it is recognized
Goal:
- Solve capatcha with our program
