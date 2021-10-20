import unittest
from countries import get_country_code

class CountriesTestCase(unittest.TestCase):
    """Tests for 'countries.py'."""

    def test_get_country_code(self):
        """Test to make sure country codes are given correctly."""
        country_code = get_country_code('United States')
        self.assertEqual(country_code, 'us')

    def test_unique_country(self):
        """
        Test to make sure country codes are given correctly,
        for countries that are not formatted correctly (e.g. Egypt)."""
        country_code = get_country_code('Egypt, Arab Rep.')
        self.assertEqual(country_code, 'eg')

unittest.main()
