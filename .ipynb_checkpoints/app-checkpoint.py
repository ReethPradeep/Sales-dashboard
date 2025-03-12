import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv(r"C:\Users\pradeepmanjula\Documents\Sales_Dash\sales_data.csv")

# Create a Dash app
app = dash.Dash(__name__)