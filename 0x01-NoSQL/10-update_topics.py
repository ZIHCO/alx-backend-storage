#!/usr/bin/env python3
"""contains update_topics def"""


def update_topics(mongo_collection, name, topics):
    """changes a doc attr"""
    if mongo_collection is not None:
        list_named_topic = mongo_collection.update_many(
                                                   {'name': name},
                                                   {$unset: "topics"},
                                                   {$set:  {"topics": topics}}
                                                   )
