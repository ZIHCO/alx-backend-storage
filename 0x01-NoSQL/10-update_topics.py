#!/usr/bin/env python3
"""contains update_topics def"""


def update_topics(mongo_collection, name, topics):
    """changes a doc attr"""
    filter_criteria = {'name': name}
    unset_old_attri = {"$unset": 'topics'}
    set_attri = {"$set": {"topics": topics}}
    if mongo_collection:
        lists = mongo_collection.find(filter_criteria)
        for doc in lists:
            doc["topics"] = topics
