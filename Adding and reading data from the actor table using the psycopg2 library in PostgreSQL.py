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

    # INSERT new data into the actor table
    insert_query = """
    INSERT INTO actor (actorno, gender, fullname, firstnames, surname, bornin, birthdate) 
    VALUES (%s, %s, %s, %s, %s, %s, %s);
    """
    new_actor_data = (2, 'M', 'Farshid Keivanian', 'Farshid', 'Keivanian', 'Esfahan', '2024-04-05')
    cursor.execute(insert_query, new_actor_data)
    conn.commit()
    print("New data inserted into the actor table successfully.")

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
