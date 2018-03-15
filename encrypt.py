#!/usr/bin/python

#called as python encrypt.py <mode> <symbol> <date offset> <file>

import sys
from alpha_vantage.timeseries import TimeSeries
import json
import datetime
import hashlib

with open(sys.argv[4],'r') as file:
	plain=file.read()

#print plain

ts = TimeSeries(key='KO7DO2WL5QRGHRM1')
data,meta_data=ts.get_daily(symbol=sys.argv[2], outputsize='compact')

seed = float(data[(datetime.date.today()+datetime.timedelta(int(sys.argv[3]))).isoformat()]['4. close'])

print seed
