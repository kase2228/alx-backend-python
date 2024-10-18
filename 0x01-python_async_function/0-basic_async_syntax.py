#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay = 10.0):
    delay = random.uniform(0, max_delay + 1)
    await asyncio.sleep(delay)
    print(delay)
