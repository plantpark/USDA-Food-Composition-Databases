import requests
import json
import time
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.usda_database
posts = db.posts
#new database for drop duplicating
dbs = client.usdanew_database
post = dbs.posts

query_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
ndbno_list = []
for i in query_list:
	url='http://api.nal.usda.gov/ndb/search/?format=json&q={}&sort=n&max=1500&offset=0&api_key=Z8ORnXXrfhlTLEPRHjg4HUFqvA0WzJx3EFDkL4zw'.format(i)
	r = requests.get(url)
	try:
		for j in r.json()['list']['item']:
			print j['ndbno']
			ndbno_list.append(j['ndbno'])
	except KeyError:
		print "KeyError happens"
		pass;
ndbno_list = list(set(ndbno_list))
print 'list to set successful!'
#api_key = ['Z8ORnXXrfhlTLEPRHjg4HUFqvA0WzJx3EFDkL4zw','f7t7OmjJwvFncR1iiGaVeAZWRpZoCTQ5qKzMIitv','MDMJnVAvvKgJMH2SQ3MgG0XiCcbmrV0WwZoBq71j','RdyTSkSZdHBRGXK8VvZdYW5WWA2XQ36mwBbJN9Qt','gfBpVQThXFiLhalSLjHaHdMN6WlQveJlsOizNqVk','iMIsXnm4Jakt207BwdOZzV7KWVXAriGhXAQNcMMk','k0kgyIrBvjpWBwyaKuf0iih4dCXriLN7MlsIrVmS','wenmHVozseNaekiEZ22oK1WEz0mRtZrORfMGyJ2T','wpU95PrYB15iOntOsZM3vzCE9w8RmCnatmJTSWwP','CQhOPs47tBeqzBkIh3pa2Ji7cT9oHqdm8mCCChAp']
ndbno_newlist = ndbno_list
for i in ndbno_newlist:
	try:
		ndbno_url = 'http://api.nal.usda.gov/ndb/reports/?ndbno={}&type=f&format=json&api_key=MDMJnVAvvKgJMH2SQ3MgG0XiCcbmrV0WwZoBq71j'.format(i)
		r = requests.get(ndbno_url)
		print 'ndbno is ',r.json()['report']['food']['ndbno']
		ndbno_newlist.remove(i)
		print i,' has been removed',len(ndbno_newlist),' has left'
		posts.insert(r.json())
	except KeyError:
		print r.json()
		time.sleep(5*60)
		pass;
j = 0
k = 0
for i in posts.find():
	if i in post.find():
		j = j + 1
		print 'i is in,and j is ',j
		pass
	else:
		print 'insert ',k
		k = k + 1
		post.insert(i)