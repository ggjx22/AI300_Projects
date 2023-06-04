# data_load.py contains class DataLoader which loads in data sets and splits it into predictor and target variables.

import pandas as pd

class DataLoader:
    
    # create constructor
    def __init__(self, path_to_data):
        # define some attributes
        self.path_to_data = path_to_data
        
    # method to load data set and returns data set as a pandas dataframe
    def load_data(self):
        data = pd.read_csv(self.path_to_data)
        print(f'Data has been sucessfully loaded from {self.path_to_data}')
        return data
    
    # method that splits the data into predictors (features) being X and target being y
    def split_data(self, data):
        X = data.drop('Loan_Status', axis=1)
        y = data['Loan_Status']
        return X, y


# # Uncomment test cases below once class is built

# ### test development ###
# path = 'object-oriented-programming/take-home-practice/data/loan_prediction.csv' # relative path to csv file

# # checks path of data
# data = DataLoader(path)
# assert data.path_to_data == path

# # checks if pandas dataframe has been loaded
# df = data.load_data()
# assert isinstance(df, pd.DataFrame)

# # check if dataset is split succesfully
# X, y = data.split_data(df)
# print(X)
# print(y)

# print('All test passed.')