#!/usr/bin/env python2

import sys
import json
import actions
import navigate
import scan

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
    resp = None
    args = {}

    cmd_splitted = cmd.split()
    action = cmd_splitted[0]
    cmd_rest = cmd_splitted[1:]


    print_key = None


################ navigatement begin ############
    if action == "w":
        resp = navigate.up()
    elif action == "e":
        resp = navigate.right_up()
    elif action == "a":
        resp = navigate.left()
    elif action == "s":
        resp = navigate.down()
    elif action == "d":
        resp = navigate.right()
    elif action == "q":
        resp = navigate.left_up()
    elif action == "z":
        resp = navigate.left_down()
    elif action == "c":
        resp = navigate.right_down()
################ navigatement end ############
    elif action == "p" or action == "pickup":
        resp = actions.pickup()
    elif action == "l" or action == "drop":
        if len(cmd_rest) < 1:
            print("Missing thing to drop")
        else:
            thingid = cmd_rest[0]
            resp = actions.drop(thingid)
    elif action == "reset":
        actions.reset()
    elif action == "scan":
        resp = scan.scan()
        if len(cmd_rest) >= 1:
            print_key = cmd_rest[0]
    else:
        print("Unknown command")

    if resp is None:
        print("Error with command.")
        return 1

    if print_key:
        resp = resp['payload']
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
            if not cmd and last_cmd:
                cmd = last_cmd
            last_cmd = cmd
            command(cmd)

    except (KeyboardInterrupt, SystemExit):
        pass
    return 0


if __name__ == '__main__':
    sys.exit(main())
