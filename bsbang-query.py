#!/usr/bin/env python3

import requests

solrQueryPath = 'http://localhost:8983/solr/bsbang/select'

params = {'q': 'name:b4401', 'defType': 'edismax'}

r = requests.post(solrQueryPath, data=params)
print(r.text)
