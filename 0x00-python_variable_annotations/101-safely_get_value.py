#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence"""


from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any,
                     default: Union[T, None] = None) -> Union[T, None]:
    """
    Retrieves a value from a dictionary if the key is present.

    Parameters:
    dct (Mapping[Any, T]): A dictionary where keys are of any type
    and values are of type T.
    key (Any): The key to look up in the dictionary.
    default (Union[T, None]): The default value
    to return if the key is not found.

    Returns:
    Union[T, None]: The value from the dictionary if the key is present,
    otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
