#!/usr/bin/env python

from post import *

def pickup():
    """Pickup the thing at the current point."""
    args = dict()
    args["target"] = "pickup"
    return post(args)


def drop(inv_id):
    """Drop the given inventory item."""
    args = dict()
    args["target"] = "drop"
    args["thingid"] = inv_id
    return post(args)
