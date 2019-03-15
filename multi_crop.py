from ij import IJ, ImageStack, ImagePlus
from ij.plugin.frame import RoiManager

# still need to check with multi-channel images if the z-projection will work as is

# pull the active image
imp = IJ.getImage()
stack = imp.getImageStack()

# display Z-projection (max intensity) if stack 
if stack.getSize() > 1:
	IJ.run("Z Project...", "projection=[Max Intensity]")

# open ROI manager and make sure ROIs appear with labels
RM = RoiManager()
rm = RM.getRoiManager()
rm.runCommand("Show All with labels")

# activate rectangle selection tool
IJ.setTool("rectangle")



# user adds all ROI
# when done:

# 0. rename ROIs
#    get number of ROIs
numroi = rm.getCount()
#    iterate through ROIs and rename with selection parameters
for r in range(numroi):
	xywh = 
	rm.rename(r,"")
# 1. export ROIs as .roi file
# 2. export ROIs as .csv file
# 3. export overlay image with ROI displayed
# 4. save ROI regions and crop original stack with those regions
# 5. save cropped stacks