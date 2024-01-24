#!/usr/bin/env python3
"""contains update_topics def"""


def update_topics(mongo_collection, name, topics):
    """changes a doc attr"""
    if mongo_collection is not None:
        list_named_topic = mongo_collection.find({'name': name})
        for doc in list_named_topic:
            doc["topics"] = topics
