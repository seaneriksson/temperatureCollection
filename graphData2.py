import pandas as pd
import plotly.express as px

df = pd.read_csv('data.csv')

fig = px.line(df, x = 'time', y = 'temperature', title='Time vs. Temperature in the Garden')
fig.show()

fig.write_html("/home/pltw57/graph.html")