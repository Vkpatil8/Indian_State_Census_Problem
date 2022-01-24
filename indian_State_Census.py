"""
@Author: Vishal Patil
@Date: 23-01-2022 13:45:00
@Last Modified by: Vishal Patil
@Last Modified time: 24-01-2022 11:45:00
@Title : Solving use case 1 test case 4
"""

import csv


class IndianCensusException(Exception):
    pass


class StateCensusAnalyser:
    @staticmethod
    def state_census_loader():
        """
            desc:    method to count number of records in file
        """
        with open("StateCensusData.csv") as data:
            state_census = csv.reader(data)
            for info in state_census:
                print(info)

    @staticmethod
    def count_number_of_records():
        """
            desc: method to check file extension
        """
        with open("StateCensusData.csv") as data:
            state_census = csv.reader(data)
            return len(list(state_census))

    @staticmethod
    def file_extension(file):
        """
         desc: method to raise exception while checking file extension
        """
        if file.endswith(".csv"):
            return ".csv"
        else:
            raise IndianCensusException("File is Invalid")

    @staticmethod
    def delimiter_validation(csv_file):
        with open(csv_file, newline="") as file_data:
            dialect = csv.Sniffer().sniff(file_data.read())
            if not dialect.delimiter == ',':
                raise IndianCensusException("Error occurred in delimiter matching")
            else:
                return dialect.delimiter

    @staticmethod
    def validate_header(csv_file):
        with open(csv_file, newline="") as file_data:
            dialect = csv.Sniffer().has_header(file_data.read())
            if dialect:
                return dialect
            else:
                raise IndianCensusException("Heading is corrupted")
                


class CSVStates:
    @staticmethod
    def state_code_loader():
        with open("StateCode.csv", "r") as data:
            state_code = csv.reader(data)
            for info in state_code:
                print(info)

    @staticmethod
    def count_number_of_records():
        with open("StateCode.csv") as data:
            state_code = csv.reader(data)
            return len(list(state_code))


if __name__ == '__main__':
    file_name = "StateCensusData.csv"
    file_name1 = "StateCode.csv"
    StateCensusAnalyser.state_census_loader()
    print(StateCensusAnalyser.count_number_of_records())
    CSVStates.state_code_loader()
    print(CSVStates.count_number_of_records())
