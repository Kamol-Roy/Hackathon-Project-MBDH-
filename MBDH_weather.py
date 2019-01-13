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

from datetime import date
import pandas as pd

start = '2010-01-01'
end ='2010-12-31'


indir = r"C:\Bike_TH\weather_raw_file"
os.chdir(indir)
fileList=glob.glob("*csv")

outfile=open(r"C:\Bike_TH\weather_dat.csv",'w')
outfile.write('date'+','+'temp'+','+'wind'+','+'vis'+','+'rain'+'\n')
for i, file in enumerate(fileList):
    print('working on:', file)
    df=pd.read_csv(file)
    for index, row in df.iterrows():
        date=str(row['date'])
        temp=str(row['Tempavg'])
        wind=str(row['Windavg'])
        vis=str(row['Visavg'])
        rain=str(row['Precip'])
        outfile.write(date+','+temp+','+wind+','+vis+','+rain+'\n')
        
outfile.close()
        
        
        
        
        
        
        
        


