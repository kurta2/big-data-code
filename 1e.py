import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/Users/ahmeterenkurt/Downloads/Trips_Full_Data.csv')

# Check the data
print(df.head())
print(df.columns)

# Summarize the data to get total number of trips for each distance category
distance_columns = ['Trips <1 Mile', 'Trips 1-3 Miles', 'Trips 3-5 Miles', 'Trips 5-10 Miles', 
                    'Trips 10-25 Miles', 'Trips 25-50 Miles', 'Trips 50-100 Miles', 'Trips 100-250 Miles', 
                    'Trips 250-500 Miles', 'Trips 500+ Miles']
total_trips_by_distance = df[distance_columns].sum()

# Plotting
plt.figure(figsize=(12, 8))
total_trips_by_distance.plot(kind='bar', color='skyblue')
plt.title('Number of Travelers by Distance-Trip Categories')
plt.xlabel('Distance Categories')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
