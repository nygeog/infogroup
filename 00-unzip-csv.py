import os
import glob
import pandas as pd
import zipfile
import zlib

td = '/Volumes/Echo/GIS/data/infogroup/CSV/'

csvList = glob.glob(td + '*bus_2012.zip')

for csvS in csvList:
	#zipfile.ZipFile(csvS).extractall(td)
	zipfile.ZipFile(csvS, allowZip64=True).extractall(td)

#Weird ZIP Error - these ZIP files need to be uncompressed manually. 
#NotImplementedError: compression type 9 (deflate64)