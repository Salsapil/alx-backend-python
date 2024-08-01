#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with a string and the square of an int or float.

    Parameters:
    k (str): The string value.
    v (Union[int, float]): The value to be squared.

    Returns:
    Tuple[str, float]: A tuple where the first element is the string `k`
                       and the second element is the square of `v` as a float.
    """
    return (k, float(v ** 2))
