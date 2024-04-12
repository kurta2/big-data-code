import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
df_distance = pd.read_csv('/Users/ahmeterenkurt/Downloads/Trips_by_Distance.csv')
df_full = pd.read_csv('/Users/ahmeterenkurt/Downloads/Trips_Full_Data.csv')

# Convert 'Week' to numeric and sort
df_distance['Week'] = pd.to_numeric(df_distance['Week'], errors='coerce')
df_full['Week of Date'] = pd.to_numeric(df_full['Week of Date'], errors='coerce')
df_distance.sort_values('Week', inplace=True)
df_full.sort_values('Week of Date', inplace=True)

# Calculate averages
avg_staying_home = df_distance.groupby('Week')['Population Staying at Home'].mean()
avg_trips_1_25_miles = df_full.groupby('Week of Date')['Trips 1-25 Miles'].mean()

# Print calculated averages
print("Average staying at home:")
print(avg_staying_home)
print("Average trips 1-25 miles:")
print(avg_trips_1_25_miles)

# Plotting the average population staying at home per week
plt.figure(figsize=(15, 7))
plt.bar(avg_staying_home.index, avg_staying_home, color='orange', width=0.4)
plt.xlabel("Week")
plt.ylabel("Average Population Staying at Home")
plt.title("Average Population Staying at Home per Week")
plt.xticks(list(avg_staying_home.index))
plt.grid(True)
plt.tight_layout()  # Adjust layout to prevent clipping of ylabel
plt.show()

# Plotting the average number of trips 1-25 miles per week
# If there are values to plot
if not avg_trips_1_25_miles.empty:
    plt.figure(figsize=(15, 7))
    plt.bar(avg_trips_1_25_miles.index, avg_trips_1_25_miles, color='skyblue', width=0.4)
    plt.xlabel("Week")
    plt.ylabel("Average Trips 1-25 Miles")
    plt.title("Average Number of Trips 1-25 Miles per Week")
    plt.xticks(list(avg_trips_1_25_miles.index))
    plt.grid(True)
    plt.tight_layout()  # Adjust layout to prevent clipping of ylabel
    plt.show()
else:
    print("No data available for trips 1-25 miles.")
