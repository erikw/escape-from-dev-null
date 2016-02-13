#!/usr/bin/env python2

from pprint import pprint
import scan
from navigate import *
import actions
import sys

target_thing = "Longsword"

def main():

    sword = None
    while not sword:

        move('down')
        area = scan.scan()
        pprint(area)

        things = scan.get_nearby_things(area)

        for thing in things:
            if thing['name'] == target_thing:
                sword = thing

    pos = scan.get_position(area)

    pprint(pos)
    pprint(sword)

    res = move_to(pos, sword)
    if res['status'] != 'SUCCESS':
        print("FAILED TO MOVE")
        pprint(res)

    actions.pickup()

    while res['status'] == 'SUCCESS':
        res = right()
        pprint(res)

    actions.drop(sword['id'])


if __name__ == '__main__':
    sys.exit(main())
