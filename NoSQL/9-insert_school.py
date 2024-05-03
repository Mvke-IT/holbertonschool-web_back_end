#!/usr/bin/env python3
"""insert a new document"""


def insert_school(mongo_collection, **kwargs):
    """insert school"""
    if mongo_collection is not None:
        return mongo_collection.insert_one(kwargs).inserted_id
