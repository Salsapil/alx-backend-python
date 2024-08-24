#!/usr/bin/env python3
"""Parameterize a unit test"""

import unittest
from utils import access_nested_map
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json


class TestGetJson(unittest.TestCase):
    """test get json"""
    # decorator that allows testing multiple inputs.
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        # temporarily replaces requests.get with a mock object.
        with patch('utils.requests.get') as mock_get:
            # creates a mock response object with a json method
            # that returns the predefined test_payload.
            # ensures that when requests.get is called, it returns mock object.
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)
            # checks requests.get was called exactly once with the correct URL.
            mock_get.assert_called_once_with(test_url)
            # the output of get_json matches the expected payload.
            self.assertEqual(result, test_payload)


class TestAccessNestedMap(unittest.TestCase):
    """class that inherits from unittest.TestCase"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """method to test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(str(err.exception), f"'{path[-1]}'")
