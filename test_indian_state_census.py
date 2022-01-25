import unittest
from indian_State_Census import *


class TestCases1(unittest.TestCase):

    def test_number_of_record(self):
        """
            desc: test the method to count number of records in file
        """
        expected1 = 30
        expected2 = 38
        self.assertEqual(StateCensusData.count_number_of_records("StateCensusData.csv"), expected1)
        self.assertEqual(StateCensusData.count_number_of_records("StateCode.csv"), expected2)

    def test_check_file_extension(self):
        """
            desc: test the method to check file extension
        """
        expected = ".csv"
        self.assertEqual(StateCensusData.file_extension("StateCensusData.csv"), expected)
        self.assertEqual(StateCensusData.file_extension("StateCode.csv"), expected)

    def test_check_file_extension_false(self):
        """
         desc: test the method to raise exception while checking file extension
        """
        method = StateCensusData.file_extension
        self.assertRaises(IndianCensusException, method, "StateCensusData.txt")
        self.assertRaises(IndianCensusException, method, "StateCode.txt")

    def test_match_delimiter(self):
        """
            desc: test the method to check delimiter
        """
        expected = ','
        self.assertEqual(StateCensusData.delimiter_validation("StateCensusData.csv"), expected)
        self.assertEqual(StateCensusData.delimiter_validation("StateCode.csv"), expected)

    def test_not_match_delimiter(self):
        """
            desc: test the method to raise exception while checking delimiter
        """
        method = StateCensusData.delimiter_validation
        self.assertRaises(IndianCensusException, method, "StateCensusData.txt")
        self.assertRaises(IndianCensusException, method, "StateCode.txt")

    def test_match_header(self):
        """
            desc: test the method to check header
        """
        expected = True
        self.assertEqual(StateCensusData.validate_header("StateCensusData.csv"), expected)
        self.assertEqual(StateCensusData.validate_header("StateCode.csv"), expected)

    def test_not_match_header(self):
        """
            desc: test the method to raise exception while checking headers
        """
        method = StateCensusData.validate_header
        self.assertRaises(IndianCensusException, method, "StateCensusData1.csv")
        self.assertRaises(IndianCensusException, method, "StateCode1.csv")

    def test_count_number_of_data(self):
        """
            desc: test the method to count number of records in list
        """
        expected = 136
        self.assertEqual(StateCensusData.state_census_data_list("StateCensusData.csv", "StateCode.csv"), expected)


if __name__ == '__main__':
    unittest.main()
