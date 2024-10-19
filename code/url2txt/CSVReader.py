import pandas as pd
import os

class CSVReader:
    def read_csv(self, csv:str) -> pd.DataFrame:
        
        self.csv: str          = csv
        self.verify_existance()

        self.df:  pd.DataFrame = pd.read_csv(self.csv)
        self.verify_data()
        
        return self.df
    
    def verify_existance(self):
        if not os.path.exists(self.csv):
            raise FileNotFoundError(f"The file '{csv}' does not exist.")
    
    def verify_data(self):
        verification_data = {
            'url'             : {'exists': True, 'non_empty': True, 'type_string': True , 'type_number': False, 'non_zero': False},
            'artist'          : {'exists': True, 'non_empty': True, 'type_string': True , 'type_number': False, 'non_zero': False},
            'title'           : {'exists': True, 'non_empty': True, 'type_string': True , 'type_number': False, 'non_zero': False},
            'browse_transpose': {'exists': True, 'non_empty': True, 'type_string': False, 'type_number': True , 'non_zero': False},
            'capo_transpose'  : {'exists': True, 'non_empty': True, 'type_string': False, 'type_number': True , 'non_zero': False},
            'id'              : {'exists': True, 'non_empty': True, 'type_string': False, 'type_number': True , 'non_zero': True },
        }
        for column in verification_data:
            if column['exists']:
                self.verify_column_exists(column)
            if column['non_empty']:
                self.verify_column_value_non_empty(column)
            if column['type_string']:
                self.verify_column_type_string(column)
            if column['type_number']:
                self.verify_column_type_number(column)
            if column['non_zero']:
                self.verify_column_value_non_zero(column)

    def verify_column_exists(self, column: str) -> None:
        if not column in self.df.columns:
            raise ValueError(f"The CSV file '{self.csv}' does not contain all the required columns.\nFirt missing column: {column}")
        
    def verify_column_value_non_empty(self, column: str) -> None:
        invalid_rows = self.df[~(self.df[column].notna())]
        if not invalid_rows.empty:
            raise ValueError(f"The column '{column}' in the CSV file '{self.csv}' should contain values.\nFirst invalid row: {invalid_rows.iloc[0]}")

    def verify_column_type_string(self, column: str) -> None:
        invalid_rows = self.df[~(self.df[column].astype(str).str.len().astype(bool))]
        if not invalid_rows.empty:
            raise ValueError(f"The column '{column}' in the CSV file '{self.csv}' should contain strings.\nFirst invalid row: {invalid_rows.iloc[0]}")
        
    def verify_column_type_number(self, column: str) -> None:
        invalid_rows = self.df[~(self.df[column].astype(str).str.isdigit())]
        if not invalid_rows.empty:
            raise ValueError(f"The column '{column}' in the CSV file '{self.csv}' should contain numbers.\nFirst invalid row: {invalid_rows.iloc[0]}")
        
    def verify_column_value_non_zero(self, column: str) -> None:
        invalid_rows = self.df[~(self.df[column].astype(int) == 0)]
        if not invalid_rows.empty:
            raise ValueError(f"The column '{column}' in the CSV file '{self.csv}' should contain non-zero values.\nFirst invalid row: {invalid_rows.iloc[0]}")