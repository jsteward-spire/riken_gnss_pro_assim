import h5py
import os

dirs = ["201805", "201806", "201807"]
#dirs = ["201808", "201809", "201810"]
#dirs = ["201811", "201812", "201901"]
#dirs = ["201902", "201903", "201904"]
#dirs = ["201905", "201906", "201907"]
#dirs = ["201908", "201909", "201910"]
#dirs = ["201911", "201912", "202001"]
#dirs = ["202002", "202003", "202004"]
#dirs = ["202005", "202006", "202007"]
#dirs = ["202008", "202009", "202010"]
for dir in dirs:
    for fn in os.listdir(dir):
        rind = fn.rfind('V06A.HDF5')
        orbitNumber = fn[rind-7:rind-1]
        f = h5py.File(os.path.join(dir, fn),'r')
        lon    = f['NS']['Longitude']
        lat    = f['NS']['Latitude']
        rr     = f['NS']['surfPrecipTotRate']
        st     = f['NS']['ScanTime']
        year   = st['Year']
        month  = st['Month']
        day    = st['DayOfMonth']
        hour   = st['Hour']
        minute = st['Minute']
        second = st['Second']
        # mid point of the scan
        mp = (lon.shape[1]-1)//2
        for i in range(lon.shape[0]):
            maxrr = max(rr[i,:])
            if maxrr > 0.1: 
                print(('{:s}'+',{:.4f}'*3+',{:}'*7).format(orbitNumber,lat[i,mp],lon[i,mp],
                    maxrr,i,year[i],month[i],day[i],hour[i],minute[i],second[i]))
