import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load dataset
df_distance = pd.read_csv('/Users/ahmeterenkurt/Downloads/Trips_by_Distance.csv')

# Convert 'Date' column to datetime for better plotting
df_distance['Date'] = pd.to_datetime(df_distance['Date'])

# Filtering data
df_10_25_trips = df_distance[df_distance['Number of Trips 10-25'] > 10000000]
df_50_100_trips = df_distance[df_distance['Number of Trips 50-100'] > 10000000]

# Plotting
fig, ax = plt.subplots(2, 1, figsize=(15, 10), sharex=True)

# Scatter plot for 'Number of Trips 10-25'
ax[0].scatter(df_10_25_trips['Date'], df_10_25_trips['Number of Trips 10-25'], color='blue', label='Trips 10-25 miles')
ax[0].set_title('Dates with More Than 10,000,000 Trips of 10-25 Miles')
ax[0].set_ylabel('Number of Trips')
ax[0].legend()
ax[0].grid(True)
ax[0].xaxis.set_major_locator(mdates.MonthLocator())
ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax[0].tick_params('x', rotation=45)

# Scatter plot for 'Number of Trips 50-100'
ax[1].scatter(df_50_100_trips['Date'], df_50_100_trips['Number of Trips 50-100'], color='orange', label='Trips 50-100 miles')
ax[1].set_title('Dates with More Than 10,000,000 Trips of 50-100 Miles')
ax[1].set_xlabel('Date')
ax[1].set_ylabel('Number of Trips')
ax[1].legend()
ax[1].grid(True)
ax[1].xaxis.set_major_locator(mdates.MonthLocator())
ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax[1].tick_params('x', rotation=45)

plt.tight_layout()
plt.show()
