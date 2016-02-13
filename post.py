import json
# import urllib3
import urllib2

# http = urllib3.PoolManager()
# https = urllib3.HTTPSConnectionPool('callofthedeep.net', port=443, cert_reqs='CERT_NONE', assert_hostname=False)
# https = urllib3.HTTPSConnectionPool('callofthedeep.net', 443, cert_reqs='CERT_NONE')


def post(args):
    url = 'https://callofthedeep.net/api/?'

    args['sessionId'] = 'd810f018-3e7a-4577-b92a-d9835d5463b9'
    for key, value in args.items():
        url += "{:s}={:s}&".format(key,value)

    url = url[:-1]

    # print(url)

    # resp = https.request('POST', url)
    # req.add_header('Content-Type', 'application/json')
    # response = urllib2.urlopen(req, json.dumps(data))
    # response = urllib3.urlopen(req, None)
    # print(resp.status)

    req = urllib2.Request(url)
    # req.add_header('Content-Type', 'application/json')
    resp = urllib2.urlopen(req, None)

    if resp.getcode() != 200:
        print("HTTP error {:d}".format(resp.getcode()))

    return resp
