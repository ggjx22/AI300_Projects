# exploratory_data_analysis.py contains class ExploreDataAnalysis which helps in basic visualisation of the data set.

from data_loader import DataLoader

class ExploreDataAnalysis:
    
    # create constructor
    def __init__(self):
        return
    
    # method that checks shape of the data set
    def get_dataset_shape(self, data):
        return data.shape
    
    # method that checks for prints out all columns of data set and reflect any missing data. If 0 means no missing data.
    def check_any_missing(self, data):
        return data.isnull().sum()
    

path = 'object-oriented-programming/take-home-practice/data/loan_prediction.csv'

data = DataLoader(path)

df = data.load_data()

### test development ###
eda = ExploreDataAnalysis()

# checks size of dataframe
print(eda.get_dataset_shape(df))
assert eda.get_dataset_shape(df) == (614,13)

# check any missing data
print(eda.check_any_missing(df))

print('All test passed.')