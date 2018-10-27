import pandas as pd

# Uncomment the following lines to create extended training csv data
# import src.RStudio.data_utils as data_util
# original_data = pd.read_csv('../../data/RStudio/train.csv', dtype={'fullVisitorId': 'str'})
# data_util.ParseGStoreData.extend_original_data_to_new_csv(data)

# Read in fullVisitorId as string for uniqueness
extended_data = pd.read_csv('../../data/RStudio/train_extended.csv', dtype={'fullVisitorId': 'str'})
