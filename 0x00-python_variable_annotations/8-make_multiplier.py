#!/usr/bin/env python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function.

    Parameters:
    multiplier (float): The multiplier value.

    Returns:
    Callable[[float], float]: A function that takes a float and returns the product of that float and the multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies a given float by the multiplier.

        Parameters:
        x (float): The value to be multiplied.

        Returns:
        float: The product of `x` and the outer multiplier.
        """
        return x * multiplier
    return multiplier_function
