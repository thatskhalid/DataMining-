import pandas as pd
import os

def load_raw_data():
    """Load raw data from the 'data/raw' directory."""
    raw_data_path = os.path.join('data', 'raw', 'car_prices.csv')  # Replace with your actual file name
    df = pd.read_csv(raw_data_path)
    return df

def clean_data(df):
    """Apply cleaning steps to the raw data."""
    # Add your cleaning logic here
    df.dropna(inplace=True)  # Example: Remove missing values
    df.drop_duplicates(inplace=True)  # Example: Remove duplicates
    # Add other cleaning steps here
    return df

def save_cleaned_data(df):
    """Save the cleaned data to the 'data/cleaned' directory."""
    cleaned_data_path = os.path.join('data', 'cleaned', 'cleaned_data.csv')
    df.to_csv(cleaned_data_path, index=False)

def main():
    df_raw = load_raw_data()    # Step 1: Load raw data
    df_cleaned = clean_data(df_raw)  # Step 2: Clean the data
    save_cleaned_data(df_cleaned)  # Step 3: Save cleaned data

if __name__ == "__main__":
    main()
