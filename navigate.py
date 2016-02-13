#!/usr/bin/env python2

import sys
import json
from post import *

SESSION_ID = '4ef7f78a-c305-471d-b139-6a1b9ddd4c7e'
ENTITY_ID = 'd4941687-ba87-4d67-9dfc-be00c67a0b36'

last_cmd = None

def scan_maze():
    """Scan the current location.

    .. Returns:
    :returns: Whatever the API returns.

    """
    args = dict()
    args["sessionid"] = SESSION_ID
    args["entityid"] = ENTITY_ID
    args["target"] = "scan"
    resp = post(args)
    for line in resp:
        print line
    return 0


def command(cmd):
    """Send a command to the server.

    .. Keyword Arguments:
    :param: cmd: String with the command.

    .. Types:
    :type: cmd: A string.

    """
    args = {}
    args['entityid'] = ENTITY_ID
    args['sessionId'] = SESSION_ID

    action = cmd.split()[0]

################ Movement begin ############
    if action == "w":
        print("Moved up")
        args['target']  = 'move'
        args['direction']  = 'up'
    elif action == "e":
        print("Moved right up")
        args['target']  = 'move'
        args['direction']  = 'rup'
    elif action == "a":
        print("Moved left")
        args['target']  = 'move'
        args['direction']  = 'l'
    elif action == "s":
        print("Moved down")
        args['target']  = 'move'
        args['direction']  = 'down'
    elif action == "d":
        print("Moved right")
        args['target']  = 'move'
        args['direction']  = 'r'
    elif action == "q":
        print("Moved left up")
        args['target']  = 'move'
        args['direction']  = 'lup'
    elif action == "z":
        print("Moved left down")
        args['target']  = 'move'
        args['direction']  = 'ldown'
    elif action == "c":
        print("Moved right down")
        args['target']  = 'move'
        args['direction']  = 'rdown'
################ Movement end ############
    elif action == "p":
        print("Pickup")
        args['target']  = 'pickup'
    elif action == "l" or action == "drop":
        print("Drop")
        parts = cmd.split()
        if not parts[1]:
            print("Missing thing to drop")
        else:
            args['target']  = 'drop'
            args['thingid'] = parts[1]
    elif action == "reset":
        print("Reset")
        args['target']  = 'reset'
    else:
        print("Wrong command")
        return 1


    post(args)
    scan_maze()
    return 0


def main():
    """Navigate the maze."""
    try:
        while True:
            cmd = sys.stdin.readline()
            cmd = cmd.strip()
            if not cmd:
                cmd = last_cmd
            last_cmd = cmd
            command(cmd)

    except (KeyboardInterrupt, SystemExit):
        pass
    return 0


if __name__ == '__main__':
    sys.exit(main())
