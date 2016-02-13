#!/usr/bin/env python2

from pprint import pprint
from scan import *
import sys

def main():
    area = scan()

    pprint(area)

if __name__ == '__main__':
    sys.exit(main())
