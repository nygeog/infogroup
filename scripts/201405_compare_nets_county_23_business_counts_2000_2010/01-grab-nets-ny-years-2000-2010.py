import pandas as pd
import numpy as np
import datetime

flddir = '/Volumes/Echo/GIS/data/infogroup/CSV/'

print 'businesses'
years = [2012] #[2000,2010]
for year in years: #range(2012,2013):
	y = str(year)
	print 'year: ' + y
	fileIn = 'infogroup_bus_'+y+'.csv' 
	fileOu = 'infogroup_bus_'+y+'_nynjpa_subset.csv'
	inCSV = flddir + fileIn
	ouCSV = flddir + fileOu
	df = pd.read_csv(inCSV, dtype = {'ZIP': object})
	df = df[(df.STATE == 'NY') | (df.STATE == 'NJ') | (df.STATE == 'PA')]
	df.to_csv(ouCSV, index=False)
	shape = df.shape
	print shape

	now = datetime.datetime.now()
	print 'finished at - ' + str(now)


