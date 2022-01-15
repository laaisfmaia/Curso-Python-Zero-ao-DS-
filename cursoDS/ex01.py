print('Hello world')
import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')
print(data.head())

print(data.shape)