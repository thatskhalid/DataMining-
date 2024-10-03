# cleaning.py
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

def clean_and_visualize(file_path):  # Accept the file path as an argument
    df = pd.read_csv(file_path)  # Load the CSV file

    # Cleaning process
    df_cleaned = df.dropna()  # Remove rows with missing values
    df_filled = df.fillna(0)  # Fill missing values with 0
    df_no_duplicates = df.drop_duplicates()  # Remove duplicates

    # Strip whitespace from columns and string values
    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    # Sample data visualization
    data = df.head(10)
    fig = go.Figure(data=[go.Table(
        header=dict(values=list(data.columns), fill_color='paleturquoise', align='left'),
        cells=dict(values=[data[col] for col in data.columns], fill_color='lavender', align='left')
    )])
    fig.show()

    # Visualization of top vehicle counts
    vehicle_counts = df.groupby(['make', 'model']).size().reset_index(name='counts')
    vehicle_counts = vehicle_counts.sort_values(by='counts', ascending=False).head(10)

    plt.figure(figsize=(10,6))
    sns.barplot(x='counts', y='make', hue='model', data=vehicle_counts, palette='viridis')
    plt.title('Top Vehicles Being Bought by Consumers')
    plt.xlabel('Number of Vehicles Bought')
    plt.ylabel('Vehicle Make')
    plt.tight_layout()
    plt.show()

    return df  # Return the cleaned DataFrame


