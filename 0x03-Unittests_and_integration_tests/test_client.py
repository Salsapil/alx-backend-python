#!/usr/bin/env python3
""" test client """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ TestGithubOrgClient """
    # run the test_org method with different organization names.
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    # patches the get_json method from the client module,
    # making it return a fixed dictiona
    @patch('client.get_json', return_value={"org": "test_org"})
    def test_org(self, org_name, mock_get_json) -> None:
        """ test organization """
        # Instantiate the client
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org

        # Ensure get_json was called once with the expected URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

        # Check that the result matches the mocked return value
        self.assertEqual(result, {"org": "test_org"})


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""
    # patches the org property of GithubOrgClient to make it a PropertyMock.
    # This allows you to mock the property and control its return value.
    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org) -> None:
        """test_public_repos_url"""
        # set to a dictionary with the key repos_url.
        # This simulates the expected response from the org property.
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test-org/repos"}

        # Instantiate the client
        client = GithubOrgClient("test-org")

        # Test the _public_repos_url property
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/orgs/test-org/repos")

        # Ensure that the org property was accessed exactly once
        mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json) -> None:
        """ test_public_repos """
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as m_url:

            m_url.return_value = "https://api.github.com/orgs/test-org/repos"

            client = GithubOrgClient("test-org")
            repos = client.public_repos()

            self.assertEqual(repos, ["repo1", "repo2", "repo3"])
            m_url.assert_called_once()

            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test-org/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected) -> None:
        """ test_has_license """
        client = GithubOrgClient("test-org")

        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)

    @patch('client.get_json')
    def test_public_repos_with_license(self, mock_get_json) -> None:
        """ test_public_repos_with_license """
        # Mock data with various licenses
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
            {"name": "repo3", "license": {"key": "apache-2.0"}}
        ]

        client = GithubOrgClient("test-org")
        repos = client.public_repos(license="apache-2.0")

        # Expected results with license "apache-2.0"
        self.assertEqual(repos, ["repo1", "repo3"])
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/test-org/repos")
