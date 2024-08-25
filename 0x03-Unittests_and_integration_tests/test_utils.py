#!/usr/bin/env python3
"""Parameterize a unit test"""

import unittest
from utils import access_nested_map
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import get_json
from unittest.mock import patch
from utils import memoize


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


class TestMemoize(unittest.TestCase):
    """Memoize class"""
    def test_memoize(self) -> None:
        """test_memoize method"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # patches the a_method of TestClass so that it returns 42
        # and allows us to track how many times it was called.
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test_instance = TestClass()

            # Access a_property twice
            result_1 = test_instance.a_property
            result_2 = test_instance.a_property

            # Check that the result is correct
            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)

            # Ensure that a_method was only called once
            mock_method.assert_called_once()
