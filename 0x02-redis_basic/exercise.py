#!/usr/bin/env python3
"""writing strings to Redis"""
from redis import Redis
from typing import Any
import uuid


class Cache:
    """defines a redis object"""

    def __init__(self) -> None:
        """instantiate a Redis client object"""
        self._redis = Redis()
        self._redis.flushdb

    def store(self, data: Any) -> str:
        """returns the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key