#!/usr/bin/env python3
"""contains update_topics def"""


def update_topics(mongo_collection, name, topics):
    """changes a doc attr"""
    filter_criteria = {'name': name}
    unset_old_attri = {"$unset": 'topics'}
    set_attri = {"$set": {"topics": topics}}
    if mongo_collection is not None:
        mongo_collection.update_many(
                                     filter_criteria,
                                     unset_old_attri,
                                    )
        mongo_collection.update_many(
                                     filter_criteria,
                                     set_attri
                                    )
    mongo_collection.update(
                            filter_criteria,
                            set_attri
                           )
