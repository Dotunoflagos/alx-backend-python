#!/usr/bin/env python3

import asyncio
import random
"""
concat
"""

async def wait_random(max_delay=10):
    if not isinstance(max_delay, (int, float)):
        raise ValueError("max_delay should be an integer or a float")

    delay = random.uniform(0, max_delay)  # Generate a random float delay
    await asyncio.sleep(delay)
    return delay
