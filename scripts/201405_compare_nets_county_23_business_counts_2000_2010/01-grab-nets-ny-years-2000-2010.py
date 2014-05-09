import pandas as pd
import numpy as np
import datetime

flddir = '/Volumes/Echo/GIS/data/infogroup/CSV/'
flddir = '/Volumes/Golf/data/infogroup/InfogroupBusinessData1997_2012/CSV/'

print 'businesses'
years = [2000,2010]
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
	

	print 'add decimals to LATT and LONG fields'
	inCSV = flddir + 'infogroup_bus_'+y+'_nynjpa_subset.csv'
	ouCSV = flddir + 'infogroup_bus_'+y+'_nynjpa_subset_xy.csv'
	df = pd.read_csv(inCSV, dtype = {'ZIP': object})
	df['lat'] = df['LATT'] * 0.000001
	df['lng'] = df['LONG'] * -0.000001
	df['uid'] = df.index + 1000001
	df = df[['uid','lat','lng']]
	df.to_csv(ouCSV, index=False)
	print 'finished at - ' + str(now)


# print 'add decimals to LATT and LONG fields'
# inCSV = '/Volumes/Echo/GIS/data/infogroup/CSV/infogroup_bus_2012_samp.csv'
# ouCSV = '/Volumes/Echo/GIS/data/infogroup/CSV/infogroup_bus_2012_samp_xy.csv'
# df = pd.read_csv(inCSV, dtype = {'ZIP': object})
# df['lat'] = df['LATT'] * 0.000001
# df['lng'] = df['LONG'] * -0.000001
# df['uid'] = df.index + 1000001
# df = df[['uid','lat','lng']]
# df.to_csv(ouCSV, index=False)