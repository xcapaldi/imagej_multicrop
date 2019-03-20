from ij import IJ, ImageStack, ImagePlus, WindowManager
from ij.plugin import ChannelSplitter

# pull the active image
imp = IJ.getImage()
stack = imp.getImageStack()
dir = IJ.getDirectory("Image")

numchannels = imp.getNChannels()

# pull each channel into an array
channels = ChannelSplitter.split(imp)

# make new titles
newtitles = []
for c in range(numchannels):
    newtitles.append(imp.title[:-4] + "_channel-" + str(c + 1) + ".tif")

# save each channel to its own file now
for c in range(numchannels):
    # keep the same image calibration
    channels[c].setCalibration(imp.getCalibration().copy())
    # save and show the cropped image
    IJ.saveAs(channels[c], "Tiff", dir + newtitles[c])
    channels[c].show()
    #WindowManager.setCurrentWindow(WindowManager.getWindow(newtitle))

# copy channels
dupchannels = []
for c in range(numchannels):
    dupchannels.append(channels[c].duplicate())

# enhance brightness and contrast
for c in range(numchannels):
    IJ.run(dupchannels[c], "Enhance Contrast", "saturated=0.35")
    dupchannels[c].show()

# setup text string for channel merge command
mergestring = "c1=DUP_" + newtitles[0]
for c in range(numchannels - 1):
    mergestring += " c" + str(c + 2) + "=DUP_" + newtitles[c + 1]
    print(c)

IJ.run("Merge Channels...", mergestring);
