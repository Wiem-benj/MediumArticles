# Dashboard
An interactive Dashboard developped with Plotly for data visualization.

Please note that the file 'Dash_board.py' is the main file of the dashboard application to be run. The second python file 'backend_logic.py' contains the functions that are called within the callback functions.

When running the dashboard:

1- Select a csv or excel file to be processed.

2- Select the chart type (Line, Scatter, Area, or Bar plot).

3- Select the xaxis of the plot (mandatory field for all the chart types)

4- Select the yaxis of the plot (mandatory field for all chart types except bar plot). For the Bar plot selecting xaxis without selecting the yaxis result in bar plot with values on the xaxis and their counts on the yaxis.

5- Select color (Optional). The color is the paramater color in the plots functions (Line, Scatter, Area, and Bar). It serves like a 3rd dimension where it gives more insights to the selected data in the xaxis and yaxis. 

Kindly note that Plotly automatically filter out any null data when plotting. In the future we may handle missing data by setting it to a specific value to make these missing data points visible in the plots.

Please kindly note that the processing of large data with more than 30k records may seems slow in this version of code especially for the case of excel files extension.

# Deployment
This developed dashboard is deployed in Render. You may visit this link to visualize its online version https://dashboard-gzkk.onrender.com
