from netCDF4 import Dataset
import os

for i in range(365):
    doy = i + 1    
    dir = "./2018.%03d" %doy
#    dir = "./2019.%03d" %doy
#    dir = "./2020.%03d" %doy
    if not os.path.isdir(dir):
        continue

    for fn in os.listdir(dir):
        if fn.startswith("polPhs"):
            ds = Dataset(os.path.join(dir, fn), 'r', format="NETCDF4")
            if ds.meanPrecipitation_06 > 0.1:
                print('{:s},{:.2f},{:.2f},{:.2f},{:},{:},{:},{:},{:},{:d}'.format(fn,ds.lat,ds.lon,ds.meanPrecipitation_06,ds.year,ds.month,ds.day,ds.hour,ds.minute,int(ds.second)))
            ds.close()
