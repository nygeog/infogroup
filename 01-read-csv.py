import pandas as pd
import numpy as np
import datetime

flddir = '/Volumes/Echo/GIS/data/infogroup/CSV/'

print 'businesses'
for year in range(2012,2013):
	y = str(year)
	fileIn = 'infogroup_bus_'+y+'.csv' 
	fileOu = 'infogroup_bus_'+y+'_samp.csv'
	inCSV = flddir + fileIn
	ouCSV = flddir + fileOu
	df = pd.read_csv(inCSV, dtype = {'ZIP': object})
	df = df.loc[np.random.choice(df.index, 50, replace=False)]
	#df = df.drop(df.index[[1,3]])
	df.to_csv(ouCSV, index=False)

	now = datetime.datetime.now()
	print 'finished at - ' + str(now)


# print 'consumers'
# for year in range(2012,2013):
# 	y = str(year)
# 	fileIn = 'infogroup_cons_'+y+'.csv' 
# 	fileOu = 'infogroup_con_'+y+'_samp.csv'
# 	inCSV = flddir + fileIn
# 	ouCSV = flddir + fileOu
# 	df = pd.read_csv(inCSV, dtype = {'ZIP': object})
# 	df = df.loc[np.random.choice(df.index, 50, replace=False)]
# 	#df = df.drop(df.index[[1,3]])
# 	df.to_csv(ouCSV, index=False)

# 	now = datetime.datetime.now()
# 	print 'finished at - ' + str(now)