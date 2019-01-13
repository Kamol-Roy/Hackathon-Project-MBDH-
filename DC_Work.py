import os
import glob
import pandas as pd
import zipfile

inpfile_start=r"C:\Bike_TH\Crash-_Data\unique_start_location_LAT_LON.csv"
inpfile_end=r"C:\Bike_TH\Crash-_Data\unique_end_location_LAT_LON.csv"


df_start=pd.read_csv(inpfile_start)
df_end=pd.read_csv(inpfile_end)

loc_dict={}

for df in [df_start, df_end]:
    
    for index, row in df.iterrows():
        if row[0] not in loc_dict:
            loc_dict[row[0]]=[row[1], row[2]]

        


OD_dict={}

indir = r"C:\Bike_TH\Raw_File"
os.chdir(indir)
fileList=glob.glob("*zip")



for filename in fileList[:]:
    
    print('working on :', filename)

    with zipfile.ZipFile(filename, 'r') as zfile:
        print(zfile.namelist()[0])
        byte_file =zfile.read(zfile.namelist()[0]).decode('utf-8').split('\n')
        for i,line in enumerate(byte_file):
            line_split=line.split(",")
            if len(line_split)>1 and i>0:
                try:
                
                    try:
                        start_loc=line_split[3]
                        end_loc=line_split[3]
                        s=tuple(loc_dict[start_loc])
                        e=tuple(loc_dict[end_loc])
        
                        if s not in OD_dict:
                            OD_dict[s]={e:1}
                        else:
                            if e not in OD_dict[s]:
                                OD_dict[s][e]=1
                            else:
                                OD_dict[s][e]+=1
    
                    except:
    
                        start_loc=line_split[2]
                        end_loc=line_split[4]
    
                        
                        if len(start_loc)>2 and len(end_loc)>2:
                            
                            s=tuple(loc_dict[start_loc])
                            e=tuple(loc_dict[end_loc])                        
        
                            if s not in OD_dict:
                                OD_dict[s]={e:1}
                            else:
                                if e not in OD_dict[s]:
                                    OD_dict[s][e]=1
                                else:
                                    OD_dict[s][e]+=1 



                except:                
                    start_loc=line_split[4]
                    end_loc=line_split[6]
                    
                    
                    if len(start_loc)>2 and len(end_loc)>2:
                        
                        s=tuple(loc_dict[start_loc])
                        e=tuple(loc_dict[end_loc])                        
                    
                        if s not in OD_dict:
                            OD_dict[s]={e:1}
                        else:
                            if e not in OD_dict[s]:
                                OD_dict[s][e]=1
                            else:
                                OD_dict[s][e]+=1                 


                    
import mplleaflet
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import pygeohash as gh                    


for s_cord in OD_dict:
    lat1,lon1=s_cord
    outgoing=0
    incoming=0
    for e_cord in OD_dict[s_cord]:
        lat2,lon2=e_cord
   
        outgoing+=OD_dict[s_cord][e_cord]
        try:
            incoming+=OD_dict[e_cord][s_cord]
        except:
            pass
    if lat1!='na' and lat2!='na':
        if outgoing>incoming:
            plt.plot(float(lon1),float(lat1),'o',c='g')
        elif outgoing==incoming:
            plt.plot(float(lon1),float(lat1),'o',c='gray')
        else:
            plt.plot(float(lon1),float(lat1),'o',c='r')
    



                    
for s_cord in OD_dict:
    
    lat1,lon1=s_cord
    
    for e_cord in OD_dict[s_cord]:
        lat2,lon2=e_cord
        wt=OD_dict[s_cord][e_cord]
    
    if lat1!='na' and lat2!='na':
        if 36<float(lat1)<44 and 36<float(lat2)<44:
            if -74>float(lon1)>-80 and -74>float(lon2)>-80:
                plt.plot([float(lon1),float(lon2)],[float(lat1),float(lat2)],color='k',lw=2)

mplleaflet.show()                    






                            
                        



