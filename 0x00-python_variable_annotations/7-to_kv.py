#!/usr/bin/env python3
"""
sum use of float
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    sum use of float
    """
    return (k, float(v * v))
