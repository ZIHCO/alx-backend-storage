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

    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """Retrieves a value from a Redis data storage"""
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> str:
        """returns a string value from a Redis data storage"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """returns an integer value from a Redis data storage"""
        return self.get(key, lambda x: int(x))
