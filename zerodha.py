import requests.packages.urllib3
import json
import time
import codecs
rq=codecs.open('firstoutput.txt','r',encoding='utf-8')
ra=rq.read()
rq.close()
ra=ra.split("\n")
for i in ra:
	ax=i.split(",")
	time.sleep( 1 )
	print ax[0]
	requests.packages.urllib3.disable_warnings()
	url = 'https://api.kite.trade/instruments/historical/'+ax[2]+'/minute?access_token=a&api_key=kitefront&from=2015-07-10&to=2015-08-09&1470743474629'
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	response = requests.get(url, headers=headers)
	p=response.content
	p=json.loads(p)
	#print p
	if len(p['data']['candles'])>0:

		fileopen=codecs.open('dump_minute_wise/'+ax[0]+'.txt','w',encoding='utf-8')
		for i in p['data']['candles']:
			#pp=i.split(",")
			aw=i[0]
			aw=aw.replace("T"," ")
			aw=aw.replace("+0530","")
			
			fileopen.write(str(aw)+","+str(i[1])+","+str(i[2])+","+str(i[3])+","+str(i[4])+","+str(i[5])+"\n")