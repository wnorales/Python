import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
'Server=NY-L-WNORALES\SQLEXPRESS;'
'Database=CCH_ENT;'
'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('Select * FROM CLIENT')

for row in cursor:
    print(row)
