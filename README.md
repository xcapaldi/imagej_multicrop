# ImageJ Multi-crop and associated utility packages

This a small ecosystem of packages scripted in jython to run in ImageJ/Fiji. They were
designed in particular to help with microscopy data preprocessing. Normally the field of
view recorded by the camera in the microscope is larger than the sample of interest and
may contain several distinct samples. Before beginning any significant data processing
we would like to crop the captured data to a reasonable size. The following three
packages should make that process much easier and faster:

## channel split

This plugin takes a multichannel tif stack and splits the channels into distinct tif
stacks. These are automaticaly saved with appropriate names in the same folder as the
original file. Then the stacks have their contrast enhanced and they are recombined into
an RGB stack which allows you to view the channels simultaneously. Currently this plugin
should be able to handle at least up to six channels although I haven't tested higher
than that. The RGB stack is NOT automatically saved. It's main purpose is to be used in
the subsequent package. Also note that the original data is not modified by the contrast
enhancement. That is just temporary to ease the preprocessing.

## multi-select

This plugin takes a tif stack and displays the Z-projection (max). It then enables the
ROI manager which allows you to draw and add multiple rectangular regions of interest.
These can be added, modified and deleted manually in the ROI manager.

# multi-crop

This plugin takes the open ROIs in the ROI manager and applies them to any number of
original datasets that you've selected. Those stacks are then automatically cropped
multiple times into the correct ROIs. These are automatically saved in the same folder
as the original file with a name ending in roi-x-y-w-h where x and y are the position
and w and h are the width and height of the region of interest. An overlay can also be
saved manually for reference if desired. Again, the raw data is not altered at all in
this process. 

## Installation

In Gnu/Linux and Windows, place the noise_subtract.py file inside the Fiji.app/plugins
folder (or any subfolder). In MacOSX go to the "Applications" folder in Finder,
right-click on the Fiji icon and select "Show package contents" to find the plugins
folder.

Then in Fiji go to Help -> Refresh Menus. You will have to restart Fiji and then the
plugin will appear in the Plugins menu.
