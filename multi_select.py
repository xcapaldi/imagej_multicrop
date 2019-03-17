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