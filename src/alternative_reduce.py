#!/usr/bin/env python3

# copied over original reduce script and visualize script before changin
# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--output_path')
parser.add_argument('--keys',nargs='+',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot
import matplotlib.dates
from datetime import datetime
import glob

# needed to change method of inputting file 
# load each of the input paths
paths = glob.glob('outputs/geoTwitter*.lang')
total = defaultdict(lambda: Counter())
D = dict()
for path in paths:
    with open(path) as f:
        date = os.path.splitext(os.path.basename(path))[0][10:18]
        tmp = json.load(f)
        for key in args.keys:
            if key in tmp:
                if key not in total:
                    total[key] = dict()
                if date not in total[key]:
                    total[key][date] = []
                totals = sum(tmp[key].values())
                total[key][date].append(totals)

print("print(total)=", print(total))
#plotting below
fig, ax = matplotlib.pyplot.subplots()
for key in args.keys:
    print("print(key)=", print(key))
    dates = sorted(total[key].keys())
    print("print(dates)=", print(dates))
    value = [sum(total[key][date]) for date in dates]
    print("print(value)=", print(value))
    DOY = [datetime.strptime(date, '%y-%m-%d') for date in dates]
    print("print(DOY)=", print(DOY))
    ax.plot(DOY ,value ,label = key)

#labels and such
#what even was args.percent
ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=4))
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%y-%m-%d'))
ax.set_xlabel("dates")
ax.set_ylabel('num. of tweets')
ax.legend()

#file name
name = [] 
for a in args.keys:
    name.append(a[1:])
final_name = '_'.join(name)
matplotlib.pyplot.savefig(final_name + '.png')
