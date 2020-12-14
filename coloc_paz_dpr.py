import pandas as pd
import datetime

# max time delta
maxtd = datetime.timedelta(minutes=30)
# max distance delta in degrees
maxd_deg = 2.0

paz_df = pd.read_csv('PAZ.csv')
dpr_df = pd.read_csv('DPR.csv')

paz_time  = pd.to_datetime({'year': paz_df['year'], 'month': paz_df['month'],
    'day': paz_df['day'], 'hour': paz_df['hour'], 'minute': paz_df['minute'],
    'second':paz_df['second']})
paz_df['time'] = paz_time

dpr_time  = pd.to_datetime({'year': dpr_df['year'], 'month': dpr_df['month'],
    'day': dpr_df['day'], 'hour': dpr_df['hour'], 'minute': dpr_df['minute'],
    'second':dpr_df['second']})
dpr_df['time'] = dpr_time

# print header information
print('PAZ_file,DPR_orbit,DPR_scan,PAZ_lat,DPR_lat,PAZ_lon,DPR_lon,PAZ_Precip,DPR_Precip,PAZ_time,DPR_time')

for index, row in paz_df.iterrows():
    # mask points within the maximum time delta
    # print('Now testing ' + str(row['time']))
    tmask = (dpr_df['time'] > row['time']-maxtd) & (dpr_df['time'] <= row['time']+maxtd)
    time_df = dpr_df.loc[tmask]
    if time_df.shape[0] == 0:
        # print('Warning: no DPR times found for {:}'.format(row['time']))
        continue

    # mask points within the maximum space delta
    dmask = ((time_df['lat']-row['lat']).pow(2) + (time_df['lon']-row['lon']).pow(2)) < maxd_deg*maxd_deg
    coloc = time_df.loc[dmask]
    if coloc.shape[0] == 0:
        continue
    else:
        for index2, row2 in coloc.iterrows():
            print(('{:}' + ',{:}'*2 + ',{:.4f}'*6 + ',{:}'*2).format(row['file'],row2['orbit'],row2['scan'],
                row['lat'],row2['lat'],row['lon'],row2['lon'],row['rr'],row2['rr'],row['time'],row2['time']))
