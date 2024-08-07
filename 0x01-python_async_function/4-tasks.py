#!/usr/bin/env python3
"""4. Tasks"""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """The code is nearly identical to wait_n
    except task_wait_random is being called."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return (sorted(delays))
