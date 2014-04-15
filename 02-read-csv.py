import csv
import pandas as pd
import numpy as np
import datetime

flddir = '/Volumes/Echo/GIS/data/infogroup/CSV/'

fileIn = 'infogroup_cons_2012.csv' 
inCSV = flddir + fileIn

reader = csv.reader(open(inCSV))


count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1
