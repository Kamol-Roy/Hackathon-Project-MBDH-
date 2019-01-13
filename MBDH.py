import pandas as pd
import h5py
import pyhdf
from pyhdf.SD import SD, SDC
import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import style
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import matplotlib.cm as cm
import math
import pickle
from osgeo import ogr, osr
from scipy.stats.stats import pearsonr
import gzip
from osgeo import ogr, osr
import zipfile
import pdb
import matplotlib.ticker as mticker
from datetime import datetime


indir = r"C:\Bike_TH\Raw_File"
os.chdir(indir)
fileList=glob.glob("*zip")


freq_dict={}



for filename in fileList[:]:
    
    print('working on :', filename)

    with zipfile.ZipFile(filename, 'r') as zfile:
        print(zfile.namelist()[0])
        byte_file =zfile.read(zfile.namelist()[0]).decode('utf-8').split('\n')
        for i,line in enumerate(byte_file):
            line_split=line.split(",")
            if len(line_split)>1 and i>0:
                try:
                    time=datetime.strptime(line_split[1].split(' ')[0],'%m/%d/%Y')
                except:
                    time=datetime.strptime(line_split[1].split(' ')[0],'%Y-%m-%d')
                if time not in freq_dict:
                    freq_dict[time]=1
                else:
                    freq_dict[time]+=1



DATE=sorted(freq_dict.keys())
freq=[]

for dt in DATE:
    freq.append(freq_dict[dt])

#DATE=[datetime.strptime(dt,'%m/%d/%Y') for dt in date]
fig=plt.figure(figsize= (16,8))
ax1 = plt.subplot2grid((3,1), (0,0), rowspan=3, colspan=1)

ax1.plot(DATE,freq,'-', color='r')


for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(90)
ax1.xaxis.set_major_locator(mticker.MaxNLocator(29))
plt.tight_layout()
plt.grid()
plt.savefig(r"C:\Bike_TH\bike_trend.png",dpi=400)
plt.show()

            

        
        
        

            
        

