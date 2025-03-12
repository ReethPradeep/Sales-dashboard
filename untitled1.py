import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Load the cleaned dataset
df = pd.read_csv('sales_data.csv')

# Create a Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Sales Dashboard"),

    # Dropdown for selecting region (if region is available in your dataset)
    dcc.Dropdown(
        id='region-dropdown',
        options=[{'label': region, 'value': region} for region in df['Region'].unique()],
        value=df['Region'].unique()[0],  # Default value
    ),

    # Graph for displaying sales over time
    dcc.Graph(id='sales-over-time-graph'),
])

# Callback to update the graph based on selected region
@app.callback(
    dash.dependencies.Output('sales-over-time-graph', 'figure'),
    [dash.dependencies.Input('region-dropdown', 'value')]
)
def update_graph(selected_region):
    # Filter data for the selected region
    filtered_df = df[df['Region'] == selected_region]
    
    # Group data by month and year, then plot
    monthly_sales = filtered_df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
    fig = px.line(monthly_sales, x='Month', y='Sales', title=f'Sales Over Time in {selected_region}')
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
