#!/usr/bin/env python3
"""
This module contains an asynchronous function
`wait_random` that waits for a random
delay between 0 and `max_delay` seconds,
and then returns the delay.

The script demonstrates how to use
asynchronous programming in Python with asyncio
to introduce delays and handle
concurrent tasks effectively.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a
    random delay and returns the delay.

    This function generates a random float number
    between 0 and `max_delay` (inclusive),
    pauses for that amount of time using `asyncio.sleep`,
    and then returns the duration
    of the delay. The delay simulates an I/O-bound
    operation or a task that takes time
    to complete.

    Args:
        max_delay (float, optional):
        The maximum delay time in seconds. Defaults to 10.0.

    Returns:
        float: The random delay duration in seconds.

    Example:
        >>> delay = await wait_random(5)
        >>> print(delay)
    """
    delay: float = random.uniform(0, max_delay + 1)
    await asyncio.sleep(delay)
    return delay
