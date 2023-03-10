#!/usr/bin/env python3
import signal

import requests


def sig_handler(signal, frame):
    exit(0)


signal.signal(signal.SIGINT, sig_handler)

flowurl = 'http://localhost:8008/flows/json?maxFlows=100&timeout=60'
flowID = -1
while 1 == 1:
    r = requests.get(flowurl + "&flowID=" + str(flowID))
    if r.status_code != 200: break
    flows = r.json()
    if len(flows) == 0: continue

    flowID = flows[0]["flowID"]
    flows.reverse()
    for f in flows:
        print(str(f['flowID']) + ',' + f['name'] + ',' + f['flowKeys'] + ',' + str(f['value']) + ',' + str(
            f['start']) + ',' + str(f['end']) + ',' + f['agent'] + ',' + str(f['dataSource']))
