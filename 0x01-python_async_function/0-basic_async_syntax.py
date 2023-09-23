#!/usr/bin/env python3
"""
concat
"""
import asyncio
import random


async def wait_random(max_delay: int=10):
    """
    concat
    """
    delay = random.uniform(0, max_delay)  # Generate a random float delay
    await asyncio.sleep(delay)
    return delay
