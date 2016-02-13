#!/usr/bin/env python2

from pprint import pprint
import scan
from navigate import *
import actions
import sys

target_thing = "Longsword"

def main():
    env = scan.scan()
    orig_inventory = scan.get_inventory(env)

    for inv in orig_inventory:
        actions.drop(inv)

    pos = scan.get_position(env)
    dest = {'x': 1, 'y': 5}
    move_to(pos, dest)

    all_things = {}

    env = scan.scan()
    things = get_nearby_things(env)
    while things:
        env = scan.scan()
        things = get_nearby_things(env)
        for thing in things:
            all_things[thing['id']] = thing

        actions.pickup()
        right()

    for orig_thing in orig_inventory:
        if orig_thing['id'] in all_things:
            del all_things[orig_thing['id']]

    sorted_things = sorted(all_things.itervalues(), key=lambda x: x['name'])
    left()
    for thing in sorted_things:
        drop[thing['id']]
        left()

if __name__ == '__main__':
    sys.exit(main())
