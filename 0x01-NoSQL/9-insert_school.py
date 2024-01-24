#!/usr/bin/env python3
"""contains insert_school"""


def insert_school(mongo_collection, **kwargs):
    """returns the new doc _id"""
    if mongo_collection:
        mongo_collection.insert_one(kwargs)
        return mongo_collection.find()[0]["_id"]
