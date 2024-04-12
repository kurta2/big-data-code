import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load datasets
df_distance = pd.read_csv('/Users/ahmeterenkurt/Downloads/Trips_by_Distance.csv')
df_full = pd.read_csv('/Users/ahmeterenkurt/Downloads/Trips_Full_Data.csv')

# Convert date columns to datetime, specifying format to avoid warnings if possible
df_distance['Date'] = pd.to_datetime(df_distance['Date'], format='%d/%m/%Y')
df_full['Week Ending Date'] = pd.to_datetime(df_full['Week Ending Date'], errors='coerce', format='%d-%b-%y')

# Check the column names and types
print(df_distance.dtypes)
print(df_full.dtypes)

# Filter data for week 32 and select columns, ensuring column names are correct
week_32_distance = df_distance[df_distance['Week'] == 32][['Number of Trips 5-10', 'Number of Trips 10-25']]
week_32_full = df_full[df_full['Week Ending Date'].dt.week == 32][['Trips 1-25 Miles', 'Trips 25-100 Miles']]

# Ensure both dataframes have data to merge
if week_32_distance.empty or week_32_full.empty:
    raise ValueError("One of the DataFrames is empty after filtering. Check the data.")

# Merge both dataframes on the 'Date' column
week_32_full['Date'] = week_32_full['Week Ending Date']  # Ensure this column exists and is named correctly
df_merged = pd.merge(week_32_distance, week_32_full, on='Date')

# Model setup
X = df_merged[['Trips 1-25 Miles']]
y = df_merged['Number of Trips 5-10']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")
