# USDA-Food-Composition-Databases
USDA Food Composition Databases
##Requirement
pymongo,usda api 

ps: The keys below I applied,please don't exceeded the rate limit 1000/h.

**api_key** = ['Z8ORnXXrfhlTLEPRHjg4HUFqvA0WzJx3EFDkL4zw','f7t7OmjJwvFncR1iiGaVeAZWRpZoCTQ5qKzMIitv','MDMJnVAvvKgJMH2SQ3MgG0XiCcbmrV0WwZoBq71j','RdyTSkSZdHBRGXK8VvZdYW5WWA2XQ36mwBbJN9Qt','gfBpVQThXFiLhalSLjHaHdMN6WlQveJlsOizNqVk','iMIsXnm4Jakt207BwdOZzV7KWVXAriGhXAQNcMMk','k0kgyIrBvjpWBwyaKuf0iih4dCXriLN7MlsIrVmS','wenmHVozseNaekiEZ22oK1WEz0mRtZrORfMGyJ2T','wpU95PrYB15iOntOsZM3vzCE9w8RmCnatmJTSWwP','CQhOPs47tBeqzBkIh3pa2Ji7cT9oHqdm8mCCChAp']

##Instruction
**query_list:**a list of strings to query in usda database.
**usda search api:**url='http://api.nal.usda.gov/ndb/search/?format=json&q={}&sort=n&max=1500&offset=0&api_key=Z8ORnXXrfhlTLEPRHjg4HUFqvA0WzJx3EFDkL4zw'.format(i)

That returns food name and database noumber'ndbno'.Only the ndbno is useful for the next query.

**Nutrient Reports API:** ndbno_url = 'http://api.nal.usda.gov/ndb/reports/?ndbno={}&type=f&format=json&api_key=MDMJnVAvvKgJMH2SQ3MgG0XiCcbmrV0WwZoBq71j'.format(i)

The target json data you should store in mongodb

For more USDA API please check https://ndb.nal.usda.gov/ndb/api/doc!


##How to use

import pandas as pd
import json
df = pd.DataFrame()
for line in open('usda.json','r'):
	df = df.append(pd.read_json(line)['report']['food'],ignore_index=True)
