#!/usr/bin/env python2

from pprint import pprint
from scan import *
import sys

def main():
    area = scan()
    pprint(area)

    things = get_nearby_things(area)

    pprint(things)

if __name__ == '__main__':
    sys.exit(main())
