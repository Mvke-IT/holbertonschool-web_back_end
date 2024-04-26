#!/usr/bin/env python3
"""
Takes a string and a number and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """create a tuple with a str and a num"""
    return (k, v**2)
