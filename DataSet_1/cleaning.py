import pandas as pd
import matplotlib.pyplot as plt #used for plots
import plotly.graph_objects as go #tables and charts in a browser
import seaborn as sns #bar plots and heatmaps


df = pd.read_csv('car_prices.csv') #loads the CSV file with the correct path



df_cleaned = df.dropna() #removes rows with missing values
df_filled = df.fillna(0) #Missing values are filled in with "0"
df_no_duplicates = df.drop_duplicates() #Duplicates are remoed

df.columns = df.columns.str.strip()  # For columns #white spaces are removed
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)  


run_block = True #runs this block of code (did this for personal testing)
if run_block:

    data = df.head(10) #retrieves first ten rows

    #the table is created here (using plotly)
    fig = go.Figure(data=[go.Table( 
        header=dict(values=list(data.columns),
                    fill_color='paleturquoise',
                    align='left'),
        cells=dict(values=[data[col] for col in data.columns],
                fill_color='lavender',
                align='left'))
    ])

    fig.show()

#First question:
#-What kind of vehicles are being bought by consumers? 
#-We will be disregarding the vehicle's condition due to the absence of proper documentaion of what the numbers mean 

vehicle_counts = df.groupby(['make', 'model']).size().reset_index(name='counts') 
#Make and model columns are grouped in the bar-graph and the size() method counts # of occurences
#a new column is made that holds these values in "count"

vehicle_counts = vehicle_counts.sort_values(by='counts', ascending=False).head(10)
#sorts the vehicle counts in descending order
#only top 10 models were showed here

plt.figure(figsize=(10,6))
sns.barplot(x='counts', y='make', hue='model', data=vehicle_counts, palette='viridis')
#x is the number of cars sold
#y is the car make
#color hue shows the specific models 

plt.title('Top Vehicles Being Bought by Consumers')
plt.xlabel('Number of Vehicles Bought')
plt.ylabel('Vehicle Make')

plt.tight_layout()
plt.show()

#print(df.head(10))


