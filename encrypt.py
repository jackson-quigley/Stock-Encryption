#!/usr/bin/python

#called as python encrypt.py <mode> <symbol> <date offset> <file>

import sys
from alpha_vantage.timeseries import TimeSeries
import datetime
import hashlib

with open(sys.argv[4],'r') as file:
	plain=file.read().replace('\n',' ')

with open('alpha_vantage_key.txt','r') as file:
	k=file.read

#print plain.replace('\n','')

ts = TimeSeries(key=k)
data,meta_data=ts.get_daily(symbol=sys.argv[2], outputsize='compact')

seed = float(data[(datetime.date.today()+datetime.timedelta(int(sys.argv[3]))).isoformat()]['4. close'])

#print seed

seed_hash = hashlib.sha512(str(seed)).hexdigest()

letter_offset = seed*100%1000%94

hash_offset = seed//1%128

#print letter_offset
#print hash_offset
#print seed_hash
#print len(plain)

out=''

for i in range(0,len(plain)):
	let=ord(plain[i])-32
	if sys.argv[1] == 'e':
		let=(let+letter_offset)%94
	elif sys.argv[1] == 'd':
		let=let-letter_offset
		if let<0:
			let=let+94
	out=out+chr(int(let)+32)
	letter_offset=(letter_offset+int(seed_hash[int(hash_offset)],16))%94
	hash_offset=(hash_offset+1)%128

print out
