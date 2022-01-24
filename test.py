

import indian_State_Census
import unittest


class TestCases(unittest.TestCase):

    def test_number_of_record(self):
        """
            desc: test the method to count number of records in file
        """
        result = indian_State_Census.StateCensusAnalyser.count_number_of_records()
        expected = 30
        self.assertEqual(expected, result)

    def test_check_file_extension(self):
        """
            desc: test the method to check file extension
        """
        result = indian_State_Census.StateCensusAnalyser.file_extension("StateCensusData.csv")
        expected = ".csv"
        self.assertEqual(result, expected)

    def test_check_file_extension_false(self):
        """
         desc: test the method to raise exception while checking file extension
        """
        result = indian_State_Census.StateCensusAnalyser.file_extension
        self.assertRaises(indian_State_Census.IndianCensusException, result, "abc.txt")
