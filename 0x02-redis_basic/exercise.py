#!/usr/bin/env python3
"""writing strings to Redis"""
from redis import Redis
from typing import Union
import uuid


class Cache:
    """defines a redis object"""

    def __init__(self):
        """instantiate a Redis client object"""
        self._redis = Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """returns the key"""
        key = uuid.uuid4().hex
        self._redis.set(key, data)
        return key
