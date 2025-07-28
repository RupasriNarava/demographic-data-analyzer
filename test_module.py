import unittest
import pandas as pd
from demographic_data_analyzer import calculate_demographic_data


class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.data = calculate_demographic_data(False)

    def test_race_count(self):
        actual = self.data['race_count'].tolist()
        expected = [27816, 3124, 1039, 311, 271]
        self.assertEqual(actual, expected, "Expected race counts to match")

    def test_average_age_men(self):
        actual = self.data['average_age_men']
        expected = 39.4
        self.assertEqual(actual, expected, "Expected average age of men to be 39.4")

    def test_percentage_bachelors(self):
        actual = self.data['percentage_bachelors']
        expected = 16.4
        self.assertEqual(actual, expected, "Expected percentage with Bachelors to be 16.4")

    def test_higher_education_rich(self):
        actual = self.data['higher_education_rich']
        expected = 46.5
        self.assertEqual(actual, expected, "Expected percentage with higher ed earning >50K to be 46.5")

    def test_lower_education_rich(self):
        actual = self.data['lower_education_rich']
        expected = 17.4
        self.assertEqual(actual, expected, "Expected percentage without higher ed earning >50K to be 17.4")

    def test_min_work_hours(self):
        actual = self.data['min_work_hours']
        expected = 1
        self.assertEqual(actual, expected, "Expected minimum work hours to be 1")

    def test_rich_percentage(self):
        actual = self.data['rich_percentage']
        expected = 10.0
        self.assertEqual(actual, expected, "Expected percentage of rich among min workers to be 10.0")

    def test_highest_earning_country(self):
        actual = self.data['highest_earning_country']
        expected = 'Iran'
        self.assertEqual(actual, expected, "Expected highest earning country to be 'Iran'")

    def test_highest_earning_country_percentage(self):
        actual = self.data['highest_earning_country_percentage']
        expected = 41.9
        self.assertEqual(actual, expected, "Expected highest earning country percentage to be 41.9")

    def test_top_IN_occupation(self):
        actual = self.data['top_IN_occupation']
        expected = 'Prof-specialty'
        self.assertEqual(actual, expected, "Expected top occupation in India to be 'Prof-specialty'")


if __name__ == "__main__":
    unittest.main()
