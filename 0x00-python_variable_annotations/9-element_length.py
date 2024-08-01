#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with each element and its length from the input iterable.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequences (e.g., lists, strings, tuples).

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, each containing a sequence from the input
                                and the length of that sequence.
    """
    return [(i, len(i)) for i in lst]
