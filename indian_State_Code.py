import csv

from Indian_State_Census_Problem.indian_State_Census import IndianCensusException


class CSVStates:
    @staticmethod
    def state_code_loader():
        """
            desc: method to load records in file
        """
        with open("StateCode.csv", "r") as data:
            state_code = csv.reader(data)
            for info in state_code:
                print(info)

    @staticmethod
    def count_number_of_records():
        """
            desc: method to count number of records in file
        """
        with open("StateCode.csv") as data:
            state_code = csv.reader(data)
            return len(list(state_code))

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


if __name__ == '__main__':
    CSVStates.state_code_loader()
    print(CSVStates.count_number_of_records())
