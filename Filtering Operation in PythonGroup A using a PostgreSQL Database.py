import psycopg2

# Database connection parameters
host = "localhost"  # or the appropriate hostname if not local
database = "PythonClass"
user = "postgres"
password = "your password"

# Connection string
conn_string = f"host={host} dbname={database} user={user} password={password}"

# Connect to the PostgreSQL database
try:
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print("Connected to the database.")

    # Create table Python_Group_A
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Python_Group_A (
        ID CHAR(4) PRIMARY KEY,
        Firstname VARCHAR(255),
        Surname VARCHAR(255),
        Position VARCHAR(255),
        Gender CHAR(6),
        RegistrationDate DATE,
        Status VARCHAR(10)
    );
    """)
    print("Table 'Python_Group_A' created successfully.")

    # Insert data into Python_Group_A table
    cursor.execute("""
    INSERT INTO Python_Group_A (ID, Firstname, Surname, Position, Gender, RegistrationDate, Status) 
    VALUES 
        ('0001', 'Farshid', 'Keivanian', 'Teacher', 'Male', '2024-05-04', 'Online'),
        ('0002', 'Sanaz', 'Jafari', 'Student', 'Female', '2024-05-04', 'Online')
    ON CONFLICT (ID) DO NOTHING;
    """)
    conn.commit()
    print("Data inserted into 'Python_Group_A' table successfully.")

    # Query to filter and display data based on gender
    cursor.execute("SELECT * FROM Python_Group_A WHERE Gender = 'Female';")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")
