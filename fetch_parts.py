#!/bin/env python

import requests
import sys
import json
from pprint import pprint

pagesize = 20

data = {
  'currentPage': '1',
  'pageSize': pagesize, # they won't reply with more than 100 items / page :c
  'keyword': sys.argv[1],
  'secondeSortName': '',
  'componentSpecification': ''
}

response = requests.post('https://jlcpcb.com/shoppingCart/smtGood/selectSmtComponentList', data=data)

js = json.loads(response.text)
total_items = js['data']['total']
sys.stderr.write(f"Total {total_items}\n")
parts = js['data']['list']

print('[')
# do some pagination to fetch all the parts
for i in range(0, total_items // pagesize):
    data['currentPage'] = i + 2
    sys.stderr.write(f"Paginating {i + 2}/{total_items // pagesize}\n")
    response = requests.post('https://jlcpcb.com/shoppingCart/smtGood/selectSmtComponentList', data=data)
    js = json.loads(response.text)
    for item in js['data']['list']:
        print(json.dumps(item, indent=4))
        sys.stdout.write(',')
print(']')
