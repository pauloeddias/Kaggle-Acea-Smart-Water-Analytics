import pandas as pd
def read_data(file):
  data_prefix = 'https://raw.githubusercontent.com/pauloeddias/Kaggle-Acea-Smart-Water-Analytics/master/data/'
  return pd.read_csv(data_prefix+file,error_bad_lines=False)