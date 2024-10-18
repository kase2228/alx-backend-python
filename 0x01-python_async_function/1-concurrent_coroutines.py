#!/usr/bin/env python3
"""
This module provides the wait_n coroutine, 
which spawns multiple instances 
of wait_random and returns their delays in sorted order.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with max_delay and return sorted delays.

    Args:
        n (int): Number of calls to wait_random.
        max_delay (int): Max delay for wait_random.

    Returns:
        List[float]: Sorted list of delays.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)



