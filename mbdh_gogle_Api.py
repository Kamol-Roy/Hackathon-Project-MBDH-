import pandas as pd
import h5py
import pyhdf
from pyhdf.SD import SD, SDC
import geocoder as gc
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
fileList = glob.glob("*zip")
outfile1=open('unique_start_location.csv','a')
outfile2=open('unique_end_location.csv','a')
outfile1.write(str('start_location')+','+str('start_lat')+','+str('start_lon')+'\n')
outfile2.write(str('end_location')+','+str('end_lat')+','+str('end_lon')+'\n')
freq_dict = {}

for filename in fileList[:]:

    print('working on :', filename)

    with zipfile.ZipFile(filename, 'r') as zfile:
        start_locs = []
        end_locs = []
        print(zfile.namelist()[0])
        byte_file = zfile.read(zfile.namelist()[0]).decode('utf-8').split('\n')
        for i, line in enumerate(byte_file):
            line_split = line.split(",")
            if len(line_split) > 1 and i > 0:
                start_loc = line[4]
                end_loc = line[6]
                # print(start_loc)
                if start_loc not in start_locs:
                    start_locs.append(start_loc)
                else:
                    pass
                if end_loc not in end_locs:
                    end_locs.append(end_loc)
                else:
                    pass
            for loc in start_locs:
                try:
                    start_lat = (gc.google(loc).latlng)[0]
                    start_lon = (gc.google(loc).latlng)[1]
                    outfile1.write(str(loc) + ',' + str(start_lat) + ',' + str(start_lon) + '\n')
                except:
                    outfile1.write(str(loc) + ',' + str('Na') + ',' + str('Na') + '\n')
            for loc in end_locs:
                try:
                    end_lat = (gc.google(loc).latlng)[0]
                    end_lon = (gc.google(loc).latlng)[1]
                    outfile1.write(str(loc) + ',' + str(end_lat) + ',' + str(end_lon) + '\n')
                except:
                    outfile1.write(str(loc) + ',' + str('Na') + ',' + str('Na') + '\n')

            outfile1.close()
            outfile2.close()
