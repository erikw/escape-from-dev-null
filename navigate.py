#!/usr/bin/env python2

import sys
from post import *

ENTITY_ID = 'd4941687-ba87-4d67-9dfc-be00c67a0b36'

last_cmd = None

def navigate_maze(cmd):
    """Send a command to the server.

    .. Keyword Arguments:
    :param: cmd: String with the command.

    .. Types:
    :type: cmd: A string.

    """
    args = {}
    args['entityid'] = ENTITY_ID
    args['target']  = 'move'

    if cmd.startswith("w"):
        print("Moved up")
        args['direction']  = 'up'
    elif cmd.startswith("e"):
        print("Moved right up")
        args['direction']  = 'rup'
    elif cmd.startswith("a"):
        print("Moved left")
        args['direction']  = 'l'
    elif cmd.startswith("s"):
        print("Moved down")
        args['direction']  = 'down'
    elif cmd.startswith("d"):
        print("Moved right")
        args['direction']  = 'r'
    elif cmd.startswith("q"):
        print("Moved left up")
        args['direction']  = 'lup'
    elif cmd.startswith("z"):
        print("Moved left down")
        args['direction']  = 'ldown'
    elif cmd.startswith("c"):
        print("Moved right down")
        args['direction']  = 'rdown'
    else:
        print("wrong command")
        return


    post(args)
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
            navigate_maze(cmd)

    except (KeyboardInterrupt, SystemExit):
        pass
    return 0


if __name__ == '__main__':
    sys.exit(main())
