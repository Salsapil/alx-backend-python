#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    # run the test_org method with different organization names.
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    # patches the get_json method from the client module,
    # making it return a fixed dictiona
    @patch('client.get_json', return_value={"org": "test_org"})
    def test_org(self, org_name, mock_get_json):
        # Instantiate the client
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Ensure get_json was called once with the expected URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

        # Check that the result matches the mocked return value
        self.assertEqual(result, {"org": "test_org"})
