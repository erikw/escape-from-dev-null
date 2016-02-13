from post import *

def move(direction):
    args = {}
    args['target']  = 'move'
    args['direction']  = direction

    resp = post(args)
    return resp

def up():
    return move("up")

def right_up():
    return move("rup")

def right():
    return move("r")

def right_down():
    return move("rdown")

def down():
    return move("down")

def left_down():
    return move("ldown")

def left():
    return move("l")

def left_up():
    return move("lup")

def move_to(begin, end):

    distance_x = begin['x'] - end['x']
    if distance_x < 0:
        direction_x = 'r'
    else:
        direction_x = 'l'

    for i in range(abs(distance_x)):
        res = move(direction_x)
        if res['status'] != 'SUCCESS':
            return res

    distance_y = begin['y'] - end['y']
    if distance_y < 0:
        direction_y = 'down'
    else:
        direction_y = 'up'

    for i in range(abs(distance_y)):
        res = move(direction_y)
        if res['status'] != 'SUCCESS':
            return res

    return res
