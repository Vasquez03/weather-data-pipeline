import pyodbc
from datetime import datetime

server = "project-weather.database.windows.net"
database = "weather-pipeline"
username = "user_admin"
password = "Edwinvasquez12!"

conn = pyodbc.connect(
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)


cursor = conn.cursor()

query = """
INSERT INTO weather_table (ciudad, temperatura, fecha)
VALUES (?, ?, ?)
"""

values = ("Cartago", 23.9, datetime.now())

cursor.execute(query, values)
conn.commit()

print("Dato insertado correctamente 🔥")

cursor.execute("SELECT * FROM weather_table")
for row in cursor.fetchall():
    print(row)

conn.close()