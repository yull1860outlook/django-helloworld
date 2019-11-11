import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=tcp:labsql1860.database.windows.net,1433;'
                      'Database=labsql-test;'
                      'Uid=yying;Pwd=Yull18601234;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM BuildVersion')

for row in cursor:
    print(row)
