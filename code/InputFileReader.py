import pandas as pd

# TODO: add verification of dataframe quality
# TODO: add type annotation to methods
# TODO: have 2 methods in total: csv2dataframe and verify_dataframe


class InputFileReader:
    def __init__(self):
        self.dataframe = None

    def read_csv(self, file_path):
        try:
            # Open, read, and close the CSV file in a single method
            df = pd.read_csv(file_path)
            return df
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except pd.errors.EmptyDataError:
            print("Empty CSV file.")
            return None

    def process_csv(self, file_path):
        # Read the CSV file and get the DataFrame
        self.dataframe = self.read_csv(file_path)

        if self.dataframe is not None:
            print("DataFrame successfully created:")
            print(self.dataframe)
            return self.dataframe
        else:
            print("DataFrame not created. Check if the file exists and is not empty.")
            return None