import pandas as pd
import datetime
from geopy.distance import geodesic

raw_coloc = pd.read_csv('paz_dpr_coloc.csv')
raw_coloc['paz_dt'] = pd.to_datetime(raw_coloc['PAZ_time'])
raw_coloc['dpr_dt'] = pd.to_datetime(raw_coloc['DPR_time'])

dists = []
timediffs = []

for index, row in raw_coloc.iterrows():
    paz_ll = pd.to_numeric((row['PAZ_lat'],row['PAZ_lon']))
    dpr_ll = pd.to_numeric((row['DPR_lat'],row['DPR_lon']))

    timediffs.append(row['dpr_dt']-row['paz_dt'])
    dists.append(geodesic(paz_ll,dpr_ll).km)

raw_coloc['dist'] = dists
raw_coloc['timediff'] = timediffs

new_coloc = raw_coloc.sort_values(by=['dist','timediff'])

print('PAZ_file,DPR_orbit,DPR_scan,PAZ_lat,DPR_lat,PAZ_lon,DPR_lon,PAZ_Precip,DPR_Precip,PAZ_time,DPR_time,dist,diff_sec')

for index, row in new_coloc.iterrows():
    td_sec = int(row['timediff'].total_seconds())

    print(('{:},{:},{:}' + (',{:.4f}' * 6) + (',{:}' * 2) + ',{:.2f},{:}').format(
        row['PAZ_file'],row['DPR_orbit'],row['DPR_scan'],row['PAZ_lat'],row['DPR_lat'],
        row['PAZ_lon'],row['DPR_lon'],row['PAZ_Precip'],row['DPR_Precip'],
        str(row['PAZ_time']),str(row['DPR_time']),row['dist'],td_sec))
