#!/usr/bin/env python2

import json
import urllib2
from post import *
import sys
from pprint import pprint

def scan(args):
    args["target"] = "scan"
    return post(args)

def get_inventory(scan):
    return scan['inventory']

def get_nearby_things(scan):
    return scan['scanthings']
