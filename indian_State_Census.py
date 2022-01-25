"""
@Author: Vishal Patil
@Date: 23-01-2022 13:45:00
@Last Modified by: Vishal Patil
@Last Modified time: 25-01-2022 12:20:00
@Title : Solving refactor 1 & test cases
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
    def state_census_data_list(file, file1):
        """
            desc: method to create new csv file to store all data
        """
        file_0 = open(file, "r")
        csv_reader0 = csv.reader(file_0)
        file_1 = open(file1, "r")
        csv_reader1 = csv.reader(file_1)

        with open("new_file.csv", "w") as a:
            csv_writer = csv.writer(a)
            for data in csv_reader0:
                csv_writer.writerow(data)

            for data1 in csv_reader1:
                csv_writer.writerow(data1)
        with open("new_file.csv", "r") as b:
            csv_reader = csv.reader(b)
            return len(list(csv_reader))


if __name__ == '__main__':
    file_name = "StateCensusData.csv"
    file_name1 = "StateCode.csv"
    StateCensusData.data_loader(file_name)
    print(StateCensusData.count_number_of_records(file_name))
    StateCensusData.data_loader(file_name1)
    print(StateCensusData.count_number_of_records(file_name1))
    print(StateCensusData.state_census_data_list(file_name, file_name1))
