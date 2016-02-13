import json
import urllib2
from tokens import *

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def post(args):
    url = 'https://callofthedeep.net/api/?'
    args['entityid'] = ENTITY_ID
    args['sessionId'] = SESSION_ID

    for key, value in args.items():
        url += "{:s}={:s}&".format(key,value)

    url = url[:-1]

    # print(url)

    req = urllib2.Request(url)
    # req.add_header('Content-Type', 'application/json')
    resp = urllib2.urlopen(req, None)
    if resp.getcode() != 200:
        print("HTTP error {:d}".format(resp.getcode()))

    return byteify(json.load(resp))['payload']
