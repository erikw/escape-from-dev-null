#!/usr/bin/env python

import sys

def navigate_maze(cmd):
    """Send a command to the server.

    .. Keyword Arguments:
    :param: cmd: String with the command.

    .. Types:
    :type: cmd: A string.

    """
    if cmd.startswith("w"):
        print("Moved up.")
    elif cmd.startswith("a"):
        print("Moved left")
    elif cmd.startswith("s"):
        print("Moved down")
    elif cmd.startswith("d"):
        print("Moved right")
    return 0


def main():
    """Navigate the maze."""
    try:
        while True:
            cmd = sys.stdin.readline()
            navigate_maze(cmd)

    except (KeyboardInterrupt, SystemExit):
        pass
    return 0


if __name__ == '__main__':
    sys.exit(main())
