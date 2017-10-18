#!/usr/bin/env python3

import argparse
import requests

solrQueryPath = 'http://localhost:8983/solr/bsbang/select'

# MAIN
parser = argparse.ArgumentParser('Run a test query against the Solr instance')
parser.add_argument('query')
args = parser.parse_args()

params = {'q': args.query, 'defType': 'edismax'}

r = requests.post(solrQueryPath, data=params)
print(r.text)
