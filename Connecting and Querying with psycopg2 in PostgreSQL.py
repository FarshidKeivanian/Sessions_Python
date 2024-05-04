import psycopg2

# Replace the following variables with your actual database credentials
host = "localhost"  # or another hostname if your database server is remote
database = "PythonClass"  # your database name, e.g., 'postgres' if it's the default PostgreSQL database
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

    # Execute a query
    cursor.execute("SELECT current_database();")

    # Fetch the results
    db_name = cursor.fetchone()[0]
    print("Current database:", db_name)

except Exception as e:
    print("An error occurred:", e)

finally:
    if conn:
        conn.close()
        print("Database connection closed.")


