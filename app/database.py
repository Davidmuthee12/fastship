import sqlite3


# make the connection
connection = sqlite3.connect("sqlite.db")
cursor = connection.cursor()

# 1.Create a table
cursor.execute("""
            CREATE TABLE IF NOT EXISTS shipment (
               id INTEGER,
               content TEXT,
               weight REAL,
               status TEXT
            )
""")

# 2. Add shipment data
cursor.execute("""
    INSERT INTO shipment
    VALUES (1243, 'Missile', 18.5, 'placed')
""")
connection.commit()

# 3. Read a shipment by id
cursor.execute("""
    SELECT * FROM shipment
    WHERE id = 1241
""")
result = cursor.fetchall()
print(result)


# close the connection when done
connection.close()
