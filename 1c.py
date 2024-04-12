import dask.dataframe as dd
import time
import matplotlib.pyplot as plt

# Define data types for the columns we're going to use
dtypes = {'Population Staying at Home': 'float64', 
          'Number of Trips 10-25': 'float64',
          'Number of Trips 50-100': 'float64'}

# Load the dataset with Dask, specifying data types
df = dd.read_csv('/Users/ahmeterenkurt/Downloads/Trips_by_Distance.csv', dtype=dtypes)

n_processors = [10, 20]
n_processors_time = {}

for processor in n_processors:
    start_time = time.time()
    
    # Set the number of partitions to match the number of processors
    df = df.repartition(npartitions=processor)
    
    # Calculate the mean population staying at home
    result_a = df['Population Staying at Home'].mean().compute()
    
    # Filter rows where the number of trips in the range of 10-25 is greater than 10 million
    df_10_25_trips = df[df['Number of Trips 10-25'] > 10000000]
    count_10_25_trips = df_10_25_trips['Number of Trips 10-25'].count().compute()
    
    # Filter rows where the number of trips in the range of 50-100 is greater than 10 million
    df_50_100_trips = df[df['Number of Trips 50-100'] > 10000000]
    count_50_100_trips = df_50_100_trips['Number of Trips 50-100'].count().compute()
    
    # Measure the time it took to perform the computations
    dask_time = time.time() - start_time
    n_processors_time[processor] = dask_time

    print(f"Results with {processor} processors took {dask_time:.2f} seconds")

# Extracting processors and times for plotting
processors = list(n_processors_time.keys())
times = list(n_processors_time.values())

plt.figure(figsize=(10, 5))
plt.bar(processors, times, color=['blue', 'orange'])
plt.xlabel('Number of Processors')
plt.ylabel('Time in seconds')
plt.title('Computational Efficiency using Dask with different processors')
plt.xticks(processors)
plt.show()
