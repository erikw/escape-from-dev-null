import json
import urllib2

data = {
        'ids': [12, 3, 4, 5, 6]
}

req = urllib2.Request('http://example.com/api/posts/create')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))
