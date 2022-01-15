
import plotly.express as px
import pandas as pd

data = pd.read_csv('datasets/kc_house_data.csv')
print(data.head())

data_mapa = data[['id','lat','long','price']]

mapa = px.scatter_mapbox(data_mapa, lat='lat',lon='long',
                         hover_name='id',
                         hover_data=['price'],
                         color_discrete_sequence=['fuchsia'],
                         zoom=3,height=300)

mapa.show()