#!/usr/bin/env python2

import sys
import json
from post import *

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

################ Movement begin ############
    if cmd.startswith("w"):
        print("Moved up")
        args['target']  = 'move'
        args['direction']  = 'up'
    elif cmd.startswith("e"):
        print("Moved right up")
        args['target']  = 'move'
        args['direction']  = 'rup'
    elif cmd.startswith("a"):
        print("Moved left")
        args['target']  = 'move'
        args['direction']  = 'l'
    elif cmd.startswith("s"):
        print("Moved down")
        args['target']  = 'move'
        args['direction']  = 'down'
    elif cmd.startswith("d"):
        print("Moved right")
        args['target']  = 'move'
        args['direction']  = 'r'
    elif cmd.startswith("q"):
        print("Moved left up")
        args['target']  = 'move'
        args['direction']  = 'lup'
    elif cmd.startswith("z"):
        print("Moved left down")
        args['target']  = 'move'
        args['direction']  = 'ldown'
    elif cmd.startswith("c"):
        print("Moved right down")
        args['target']  = 'move'
        args['direction']  = 'rdown'
################ Movement end ############
    elif cmd.startswith("p"):
        print("Pickup")
        args['target']  = 'pickup'
    elif cmd.startswith("l"):
        print("Drop")
        args['target']  = 'drop'
    elif cmd.startswith("i"):
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
