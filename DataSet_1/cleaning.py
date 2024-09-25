import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Load the CSV file
df = pd.read_csv('DataSet_1/car_prices.csv')



df_cleaned = df.dropna()

df_filled = df.fillna(0)  # Filling with 0

df_no_duplicates = df.drop_duplicates()

df.columns = df.columns.str.strip()  # For columns
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  # For data entries


# Get the first 10 entries
data = df.head(10)

# Create the table
fig = go.Figure(data=[go.Table(
    header=dict(values=list(data.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[data[col] for col in data.columns],
               fill_color='lavender',
               align='left'))
])

# Show the figure
fig.show()


#print(df.head(10))


