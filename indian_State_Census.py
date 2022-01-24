"""
@Author: Vishal Patil
@Date: 23-01-2022 13:45:00
@Last Modified by: Vishal Patil
@Last Modified time: 24-01-2022 19:00:00
@Title : Solving use refactor 1
"""

import csv


class IndianCensusException(Exception):
    pass


class StateCensusData:
    @staticmethod
    def data_loader(file):
        """
            desc: method to load records in file
        """
        with open(file) as data:
            state_census = csv.reader(data)
            for info in state_census:
                print(info)

    @staticmethod
    def count_number_of_records(file):
        """
            desc: method to count number of records in file
        """
        with open(file) as data:
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
        """
            desc: the method to check delimiter validation
        """
        with open(csv_file, newline="") as file_data:
            dialect = csv.Sniffer().sniff(file_data.read())
            if not dialect.delimiter == ',':
                raise IndianCensusException("Error occurred in delimiter matching")
            else:
                return dialect.delimiter

    @staticmethod
    def validate_header(csv_file):
        """
            desc: the method to check header validation
        """
        with open(csv_file, newline="") as file_data:
            dialect = csv.Sniffer().has_header(file_data.read())
            if dialect:
                return dialect
            else:
                raise IndianCensusException("Heading is corrupted")

    @staticmethod
    def state_code_loader():
        """
            desc: method to load records in file
        """
        with open("StateCode.csv", "r") as data:
            state_code = csv.reader(data)
            for info in state_code:
                print(info)


if __name__ == '__main__':
    file_name = "StateCensusData.csv"
    file_name1 = "StateCode.csv"
    StateCensusData.data_loader(file_name)
    print(StateCensusData.count_number_of_records(file_name))
    StateCensusData.data_loader(file_name1)
    print(StateCensusData.count_number_of_records(file_name1))
