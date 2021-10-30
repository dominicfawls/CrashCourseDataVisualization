import unittest
import python_repos

class CountriesTestCase(unittest.TestCase):
    """Tests for 'python_repos.py'."""

    def test_status_code(self):
        """Test to make sure the status code is 200."""
        status_code = python_repos.test_status
        self.assertEqual(status_code, 200)

    def test_item_amount(self):
        """Test to make sure 30x repository info is returned."""
        item_number = python_repos.test_length
        self.assertEqual(item_number, 30)

    def test_repositories_amount(self):
        """Test to make sure total repositories > 7,000,000."""
        item_number = python_repos.total_repositories
        self.assertGreater(item_number, 7000000)

unittest.main()
