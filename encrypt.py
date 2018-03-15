#!/usr/bin/python

#called as python encrypt.py <mode> <date offset> <file>

import sys
from alpha_vantage.timeseries import TimeSeries
import json
import datetime

with open(sys.argv[3],'r') as file:
	plain=file.read()

print plain
