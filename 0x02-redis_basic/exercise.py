#!/usr/bin/env python3
"""writing strings to Redis"""
import redis
from typing import Union
import uuid
from functools import wraps


class Cache:
    """defines a redis object"""

    def __init__(self):
        """instantiate a Redis client object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """returns the key"""
        key = uuid.uuid4().hex
        self._redis.set(key, data)
        return key
