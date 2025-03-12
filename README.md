# Sales Dashboard

## Project Overview
The Sales Dashboard project is a web-based visualization tool built using Dash, Plotly, and Pandas to provide insights into sales data. This dashboard allows users to explore sales trends across various regions, view sales performance over time, and analyze key metrics such as revenue and sales volume. It integrates a dataset that has been cleaned and preprocessed to offer an interactive and user-friendly experience.

## Key Features
+ **Sales Overview:** Provides an interactive graph displaying sales over time for selected regions.
+ **Region-based Filtering:** Allows users to filter data based on the selected region and update the visualizations accordingly.
+ **Sales Trends:** Displays sales performance trends using line charts for better understanding of seasonal variations and growth.

## Technologies Used
+ **Dash** (for building interactive web dashboards)
+ **Plotly** (for creating interactive and visually appealing charts)
+ **Pandas** (for data manipulation and cleaning)

## Project Structure
├── data/
│   ├── sales_data_cleaned.csv         
├── app/
│   ├── app.py                       
├── requirements.txt                  
├── README.md

## How to Run
1. **Clone the repository:** git clone <repository_url>
2. **Install dependencies:** First, install the necessary Python dependencies: pip install -r requirements.txt
3. **Run the Sales Dashboard:** To run the dashboard, execute the following script: python app/app.py
4. **Access the Dashboard:** Once the server is running, open your web browser and navigate to: http://127.0.0.1:8050/

## Results
+ **Interactive Dashboard:** Users can select regions, explore sales data, and view sales trends in real-time.
+ **Sales Insights:** The dashboard provides a clear view of sales performance over time, helping decision-makers understand trends and patterns in the sales data.
