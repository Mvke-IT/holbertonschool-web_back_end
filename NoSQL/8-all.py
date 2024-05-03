#!/usr/bin/env python3
"""list of all collectiosn"""


def list_all(mongo_collection):
    """return a list"""
    return list(mongo_collection.find())
