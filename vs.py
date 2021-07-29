import pandas as pd 
import csv 
import plotly.graph_object as go 


df = pd.read_csv('data.csv')

fig = go.Figure(go.Bar(

    x = df.groupby('level')['attempt'].mean(),
    y = ['student_id'],
    orientation = 'h' 
))


