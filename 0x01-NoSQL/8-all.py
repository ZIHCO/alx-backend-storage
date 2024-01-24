#!/usr/bin/env python3
"""Script contain list_all def"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """return a list of all docs"""
    if mongo_collection:
        return mongo_collection.find()
    return []
