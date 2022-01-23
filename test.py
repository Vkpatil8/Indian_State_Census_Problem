import indian_State_Census
import unittest


class TestCases(unittest.TestCase):
    def test_number_of_record(self):
        result = indian_State_Census.StateCensusAnalyser.count_number_of_records()
        expected = 30
        self.assertEqual(expected, result)

    def test_check_file_extension(self):
        result = indian_State_Census.StateCensusAnalyser.file_extension()
        expected = ".csv"
        self.assertEqual(result, expected)

    def test_check_file_extension_false(self):
        result = indian_State_Census.StateCensusAnalyser.file_extension()
        expected = ".txt"
        self.assertNotEqual(result, expected)

