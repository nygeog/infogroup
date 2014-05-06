df <- read.csv(file="/Volumes/Golf/data/infogroup/InfogroupBusinessData1997_2012/CSV/infogroup_cons_2012.csv",nrows=2000)
write.csv(df, file = "/Volumes/Golf/data/infogroup/InfogroupBusinessData1997_2012/CSV/infogroup_cons_2012_first_2000_rows.csv",row.names=FALSE)
df <- read.csv(file="/Volumes/Golf/data/infogroup/InfogroupBusinessData1997_2012/CSV/infogroup_bus_2012.csv",nrows=2000)
write.csv(df, file = "/Volumes/Golf/data/infogroup/InfogroupBusinessData1997_2012/CSV/infogroup_bus_2012_first_2000_rows.csv",row.names=FALSE)