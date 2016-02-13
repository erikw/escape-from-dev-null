#!/usr/bin/env python2

import sys
import json
from post import *
from pprint import pprint
from tokens import *


last_cmd = None

def command(cmd):
    """Send a command to the server.

    .. Keyword Arguments:
    :param: cmd: String with the command.

    .. Types:
    :type: cmd: A string.

    """
    args = {}

    cmd_splitted = cmd.split()
    action = cmd_splitted[0]
    cmd_rest = cmd_splitted[1:]


    print_key = None

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
    elif action == "scan":
        print("Scan")
        args["target"] = "scan"
        if len(cmd_rest) >= 1:
            print_key = cmd_rest[0]
    else:
        print("Wrong command")
        return 1


    resp = post(args)
    if print_key:
        if print_key in resp:
            pprint(resp[print_key])
        else:
            print("Selected key %s does not exists" % print_key)
    else:
        pprint(resp)
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
