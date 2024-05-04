import psycopg2

# Replace the following variables with your actual database credentials
host = "localhost"  # or another hostname if your database server is remote
database = "Actor"  # your database name, make sure this matches exactly
user = "postgres"  # your username
password = "your password"  # the password you use to access the database

# Connection string
conn_string = f"host={host} dbname={database} user={user} password={password}"

# Connect to the database
conn = None
try:
    conn = psycopg2.connect(conn_string)
    print("Connected to the database.")

    # Create a cursor object
    cursor = conn.cursor()

    # Execute a query to read data from the actor table
    cursor.execute("SELECT * FROM actor")

    # Fetch all rows from the table
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

except Exception as e:
    print("An error occurred:", e)

finally:
    if conn:
        conn.close()
        print("Database connection closed.")
