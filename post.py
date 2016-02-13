import json
import urllib2


def post(args):
    url = 'https://callofthedeep.net/api/?'

    for key, value in args.items():
        url += "{:s}={:s}&".format(key,value)

    url = url[:-1]

    # print(url)

    req = urllib2.Request(url)
    # req.add_header('Content-Type', 'application/json')
    resp = urllib2.urlopen(req, None)
    if resp.getcode() != 200:
        print("HTTP error {:d}".format(resp.getcode()))

    return resp
