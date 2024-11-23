import pandas as pd
import pyodbc

# Define connection parameters
server = 'DESKTOP-2UAHBMR\\SQLSERVER2022'  # Use your actual server name with the correct instance name
database = 'TestDB'  # Your database name
driver = '{ODBC Driver 17 for SQL Server}'  # Ensure you have the correct ODBC driver installed

# Establish the connection using Windows Authentication (Trusted Connection)
connection = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
)

# Define the SQL query
query = """
SELECT * FROM Book_Reviews
WHERE Rating IS NULL OR Review_Text = '';
"""

# Load data into a Pandas DataFrame
data = pd.read_sql(query, connection)

# Fill missing ratings with the average rating
data['Rating'].fillna(data['Rating'].mean(), inplace=True)

# Drop rows with missing Review_Text
data.dropna(subset=['Review_Text'], inplace=True)

# Display the cleaned data
print(data)

# Close the connection
connection.close()
