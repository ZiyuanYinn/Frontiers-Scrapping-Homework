url = "https://tracreports.org/phptools/immigration/closure/graph.php"

params = {
    "stat": "count",
    "timescale": "fymon",
    "agegrp": "2",
    "state": "All",
    "represented": "2",
    "timeunit": "percent",
    }


from pprint import pprint
import requests
#import re
#import json
import pandas as pd

response = requests.get(url, params=params)

##print("Status:", response.status_code)
##print("Final URL:", response.url)
##print("Content-Type:", response.headers.get("Content-Type"))


data = response.json()

timeline = data.get('timeline')
df = pd.DataFrame(timeline)

df = df.rename(columns={
    'fymon': 'date',
    'number': 'case_count',
    'percent': 'percent'
    })
df["case_count"] = df["case_count"].astype(int)
df["percent"] = df["percent"].astype(float)

df.to_csv("trac__children_representation.csv", index=False)


##num_entries = len(data.get('timeline'))
##timeline = data.get('timeline')
##for i in range (num_entries):
##    x = timeline[i]
##    date = x.get('fymon')
##    number = x.get('number')
##    percent = float(x.get('percent'))
    

    




##print (len(data.get('timeline')))






#print (type (data.get('timeline')[0]))
#print (type (data))
#pprint (data)
