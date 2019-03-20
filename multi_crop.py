from ij import IJ, ImageStack, ImagePlus, WindowManager
from ij.plugin.frame import RoiManager
from ij.gui import GenericDialog

# dialog to select origin window
def selectorigin():
    windows = WindowManager.getImageTitles()
    numwindows = WindowManager.getWindowCount()
    gd = GenericDialog("Multicrop")
    gd.addCheckboxGroup(numwindows, 1, windows, [False]*numwindows)
    gd.showDialog()
    # check if user canceled operations
    if gd.wasCanceled():
    	return
    # otherwise
    origin = []
    for b in range(numwindows):
        if gd.getNextBoolean() == True:
            origin.append(WindowManager.getWindow(windows[b]))
    return origin

# switch to ROI manager
RM = RoiManager()
rm = RM.getRoiManager()
# create empty array for ROIs
cropcoords = []
# export ROIs as array
roistrings = rm.getRoisAsArray()
# convert to arrays with integers and the form [[x,y,w,h],[x,y,w,h]]
numrois = rm.getCount()
for r in range(numrois):
    cropcoords.append([])
    string1 = str(roistrings[r])
    string2 = string1.split("[")[1].split("]")
    string3 = string2[0].split(",")
    for c in range(4):
        cropcoords[r].append(int(string3[c + 1].split("=")[1]))

# close ROI manager
rm.close()
# imagej will ask whether to save to overlay
# User can choose whether to keep and then save the image manually
# for reference later if desired.

# select origin windows
origins = selectorigin()

for o in range(len(origins)):
    # switch to origin window
    #WindowManager.putBehind()
    WindowManager.setCurrentWindow(origins[o])

    # get image directory
    dir = IJ.getDirectory("Image")

    # pull the origin window in
    imp = IJ.getImage()
    stack = imp.getImageStack()

    # iterate through ROIs
    for p in range(numrois):
        # set the ROIs
        imp.setRoi(cropcoords[p][0],cropcoords[p][1],cropcoords[p][2],cropcoords[p][3])
        # change the title
        newtitle = (imp.title[:-4] + "_roi-" + str(cropcoords[p][0]) + "-"
                                             + str(cropcoords[p][1]) + "-"
                                             + str(cropcoords[p][2]) + "-"
                                             + str(cropcoords[p][3]) + ".tif")
        # duplicate and crop image
        cropimp = imp.duplicate()
        # keep the same image calibration
        cropimp.setCalibration(imp.getCalibration().copy())
        # save and show the cropped image
        IJ.saveAs(cropimp, "Tiff", dir + newtitle)
        cropimp.show()
