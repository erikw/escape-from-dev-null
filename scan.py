#!/usr/bin/env python2
from post import *

def scan():
    args = {}
    args["target"] = "scan"
    return post(args)

def get_inventory(scan):
    return scan['payload']['inventory']

def get_nearby_things(scan):
    return scan['payload']['scanthings']

def get_position(scan):
    return {
             'x': scan['payload']['x'],
             'y': scan['payload']['y']
           }
