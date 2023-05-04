#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

# isolates top 10 observations and their value, then rank low to high
top_ten = items[0:10]
obs = [x[0] for x in top_ten]
values = [x[1] for x in top_ten]
obs = obs[::-1]
values = values[::-1]

matplotlib.pyplot.bar(range(len(obs)), values,)
matplotlib.pyplot.xticks(range(len(obs)), obs)

if args.input_path[-1] == 'y':
    matplotlib.pyplot.xlabel("country")
else:
    matplotlib.pyplot.xlabel("language")
if args.percent:
    matplotlib.pyplot.ylabel('percent of total tweets')
else:
    matplotlib.pyplot.ylabel('num. of tweets')

if args.input_path[-1] == 'y':
    matplotlib.pyplot.savefig(args.key[1:] + '_country.png')
else:
    matplotlib.pyplot.savefig(args.key[1:] + '_lang.png')
