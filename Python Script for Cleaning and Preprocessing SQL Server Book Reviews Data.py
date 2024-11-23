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

# Define the SQL query to select rows with NULL Rating or empty Review_Text
query = """
SELECT * FROM Book_Reviews
WHERE Rating IS NULL OR Review_Text = '';
"""

# Load data into a Pandas DataFrame
data = pd.read_sql(query, connection)

# Fill missing ratings with the average rating
data['Rating'].fillna(data['Rating'].mean(), inplace=True)

# Drop rows with missing Review_Text
cleaned_data = data.dropna(subset=['Review_Text'])

# Define a cursor for database updates
cursor = connection.cursor()

# Update the Rating values in the database
for index, row in cleaned_data.iterrows():
    cursor.execute(
        """
        UPDATE Book_Reviews
        SET Rating = ?
        WHERE Review_ID = ?
        """,
        row['Rating'], row['Review_ID']
    )

# Delete rows with missing Review_Text in the database
cursor.execute(
    """
    DELETE FROM Book_Reviews
    WHERE Review_Text = '';
    """
)

# Commit the changes to the database
connection.commit()

# Display the cleaned data
print(cleaned_data)

# Close the connection
cursor.close()
connection.close()
