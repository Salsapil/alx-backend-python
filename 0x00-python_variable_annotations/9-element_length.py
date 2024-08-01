#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples with each element and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples,
                                and the length of that sequence.
    """
    return [(i, len(i)) for i in lst]
