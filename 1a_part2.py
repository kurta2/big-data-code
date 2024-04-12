import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df_full = pd.read_csv('/Users/ahmeterenkurt/Downloads/Trips_Full_Data.csv')

# Filter out rows where 'Week Ending Date' is NaN (if needed, adjust based on your DataFrame)
df_full = df_full.dropna(subset=['Week Ending Date'])

# Assuming 'Week of Date' can be derived from 'Week Ending Date'
df_full['Week of Date'] = pd.to_datetime(df_full['Week Ending Date']).dt.isocalendar().week

# Convert trip distance columns to numeric, coerce errors to NaN
distance_columns = [
    'Trips <1 Mile', 'Trips 1-3 Miles', 'Trips 3-5 Miles', 'Trips 5-10 Miles',
    'Trips 10-25 Miles', 'Trips 25-50 Miles', 'Trips 50-100 Miles',
    'Trips 100-250 Miles', 'Trips 250-500 Miles', 'Trips 500+ Miles'
]
for column in distance_columns:
    df_full[column] = pd.to_numeric(df_full[column], errors='coerce')

# Calculate the sum of all trips for each distance category across all weeks
sum_trips_by_distance = df_full[distance_columns].sum()

# Create a histogram where x-axis is distance categories and y-axis is the sum of trips
plt.figure(figsize=(15, 7))
plt.bar(distance_columns, sum_trips_by_distance, color='skyblue')
plt.xlabel("Distance Category")
plt.ylabel("Total Number of Trips")
plt.title("Total Number of Trips by Distance Category")
plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
plt.grid(True)
plt.tight_layout()
plt.show()
