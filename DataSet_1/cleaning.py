import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns

# Load the CSV file
df = pd.read_csv('DataSet_1/car_prices.csv')



df_cleaned = df.dropna()

df_filled = df.fillna(0)  # Filling with 0

df_no_duplicates = df.drop_duplicates()

df.columns = df.columns.str.strip()  # For columns
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  # For data entries


run_block = False #ima use this instead of commenting the following block of code out
if run_block:
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

#First question:
#-What kind of new vehicles are being bought by consumers? 
#-We will be disregarding the vehicle's condition due to the absence of proper documentaion of what the numbers mean 

vehicle_counts = df.groupby(['make', 'model']).size().reset_index(name='counts')

# Sort the data to get the most popular makes/models
vehicle_counts = vehicle_counts.sort_values(by='counts', ascending=False).head(10)

# Create the bar plot using Seaborn
plt.figure(figsize=(10,6))
sns.barplot(x='counts', y='make', hue='model', data=vehicle_counts, palette='viridis')

# Add titles and labels
plt.title('Top Vehicles Being Bought by Consumers')
plt.xlabel('Number of Vehicles Bought')
plt.ylabel('Vehicle Make')

# Display the plot
plt.tight_layout()
plt.show()

#print(df.head(10))


