#!/usr/bin/env python3
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a list of integers and floating-point numbers.

    Parameters:
    mxd_lst (List[Union[int, float]]): A list containing integers and floats.

    Returns:
    float: The sum of the list as a float.
    """
    return (sum(mxd_lst))
