import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the real-world dataset from a remote URL (e.g., a GitHub Gist)
# In a real scenario, you would download this from Kaggle: https://www.kaggle.com/datasets/programmer3/smart-manufacturing-process-data
try:
    url = 'https://gist.githubusercontent.com/ajizaguirre/bf04d6229e0d3674da9b5602c5758933/raw/221199b086e39c8718f5b6df02ab8ff909a4e598/manufacturing_data.csv' # Dataset loaded into a github gist in order to use
    
    df = pd.read_csv(url)
except:
    # As a fallback for this example, we'll generate a sample dataframe that mimics the structure
    print("Could not fetch remote data. Generating a sample dataframe for demonstration.")
    data = {
        'Timestamp': pd.to_datetime(pd.date_range(start='2025-01-01', periods=1000, freq='min')),
        'Temperature_C': np.random.uniform(60, 100, 1000),
        'Machine_Speed_RPM': np.random.randint(1200, 1800, 1000),
        'Production_Quality_Score': np.random.uniform(70, 100, 1000),
        'Vibration_Level_mms': np.random.uniform(0, 1, 1000),
        'Energy_Consumption_kWh': np.random.uniform(5, 20, 1000),
        'Optimal_Conditions_Flag': np.random.randint(0, 2, 1000)
    }
    df = pd.DataFrame(data)


# --- Data Cleaning and Preparation ---
df.columns = df.columns.str.replace(' \(mm/s\)', '_mms', regex=True)
df.columns = df.columns.str.replace(' \(RPM\)', '_RPM', regex=True)
df.columns = df.columns.str.replace(' \((°C|kWh)\)', '', regex=True)
df.columns = df.columns.str.replace(' ', '_')

# Convert Timestamp to datetime object
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Check for missing values
print("Missing values in each column:\n", df.isnull().sum())

# Basic statistics
print("\nDataset Description:\n", df.describe())
