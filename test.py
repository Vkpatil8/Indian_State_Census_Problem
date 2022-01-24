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
        method = indian_State_Census.StateCensusAnalyser.file_extension
        self.assertRaises(indian_State_Census.IndianCensusException, method, "abc.txt")

    def test_match_delimiter(self):
        """
            desc: test the method to check delimiter
        """
        expected = ','
        result = indian_State_Census.StateCensusAnalyser.delimiter_validation("StateCensusData.csv")
        self.assertEqual(result, expected)

    def test_not_match_delimiter(self):
        """
            desc: test the method to raise exception while checking delimiter
        """
        method = indian_State_Census.StateCensusAnalyser.delimiter_validation
        self.assertRaises(indian_State_Census.IndianCensusException, method, "StateCensusData.txt")
