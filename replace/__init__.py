#!/usr/bin/env python
import public


@public.add
def replace(source, replacement):
    """replace multiple elements/substrings and return result"""
    if isinstance(source, (list, set, tuple)):
        for old, new in replacement.items():
            if old in source:
                source = [new if el == old else el for el in source]
    if isinstance(source, str):
        for old, new in replacement.items():
            source = source.replace(old, new)
    return source
