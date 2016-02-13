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
