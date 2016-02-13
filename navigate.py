from post import *

def move(direction):
    args = {}
    args['target']  = 'move'
    args['direction']  = 'rup'

    resp = post(args)


