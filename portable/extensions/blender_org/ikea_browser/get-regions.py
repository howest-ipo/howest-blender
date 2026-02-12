#!/usr/bin/env python3

import urllib.request
import json

data = urllib.request.urlopen("https://www.ikea.com/global/en/shared-data/regions.js").read().decode()
js = json.loads(data.split(" = ", 1)[1])

d = {}
for r in js:
    d[r['siteName']] = {ls['language']: ls['url'] for ls in r['localizedSites']}

with open("regions.json", "w") as fp:
    json.dump(d, fp)
