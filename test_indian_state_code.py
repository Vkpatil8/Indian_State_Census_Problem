import indian_State_Code
import unittest


class TestCases2(unittest.TestCase):

    def test_number_of_record(self):
        """
            desc: test the method to count number of records in file
        """
        result = indian_State_Code.CSVStates.count_number_of_records()
        expected = 38
        self.assertEqual(expected, result)

    def test_check_file_extension(self):
        """
            desc: test the method to check file extension
        """
        result = indian_State_Code.CSVStates.file_extension("StateCode.csv")
        expected = ".csv"
        self.assertEqual(result, expected)

    def test_check_file_extension_false(self):
        """
         desc: test the method to raise exception while checking file extension
        """
        method = indian_State_Code.CSVStates.file_extension
        self.assertRaises(indian_State_Code.IndianCensusException, method, "StateCode.txt")

    def test_match_delimiter(self):
        """
            desc: test the method to check delimiter
        """
        expected = ','
        result = indian_State_Code.CSVStates.delimiter_validation("StateCode.csv")
        self.assertEqual(result, expected)

    def test_not_match_delimiter(self):
        """
            desc: test the method to raise exception while checking delimiter
        """
        method = indian_State_Code.CSVStates.delimiter_validation
        self.assertRaises(indian_State_Code.IndianCensusException, method, "StateCode.txt")

    def test_match_header(self):
        """
            desc: test the method to check header
        """
        expected = True
        result = indian_State_Code.CSVStates.validate_header("StateCode.csv")
        self.assertEqual(result, expected)

    def test_not_match_header(self):
        """
            desc: test the method to raise exception while checking headers
        """
        method = indian_State_Code.CSVStates.validate_header
        self.assertRaises(indian_State_Code.IndianCensusException, method, "StateCode1.csv")


if __name__ == '__main__':
    unittest.main()
