#!/usr/bin/env python3
"""Calculate the sum of a mixed list of integers and floats."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum all nums in a mixted list"""
    return sum(mxd_lst)
