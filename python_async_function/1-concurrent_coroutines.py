#!/usr/bin/env python3
""" This async function takes 2 int. Return the list of the delay.  """
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Store  the results in a list. """
    routines = [randwait(max_delay) for i in range(n)]
    return [await x for x in asyncio.as_completed(routines)]
