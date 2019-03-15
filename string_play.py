from ij.plugin.frame import RoiManager

RM = RoiManager()
rm = RM.getRoiManager()

rois = rm.getRoisAsArray()
print(len(rois))
print(rois)
string1 = str(rm.getRoisAsArray()[1])

print(string1)
# remove brackets
string3 = string1.split("[")[1].split("]")
# remove commas
string4 = string3[0].split(",")
print(string4)
string5 = string4[1].split("=")[1] + "-" + string4[2].split("=")[1] + "-" + string4[3].split("=")[1] + "-" + string4[4].split("=")[1]
		
stringx = string4[1].split("=")[1]
stringy = string4[2].split("=")[1]
stringw = string4[3].split("=")[1]
stringh = string4[4].split("=")[1]

print(string5)
#print(stringx)
#print(stringy)
#print(stringw)
#print(stringh)
#print(stringx + "-" + stringy + "-" + stringw + "-" + stringh)
#string2 = string1[18:20]
#print(string2)
#print(string2[0])
#print(string2[1])