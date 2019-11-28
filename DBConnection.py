import pyodbc
from googlesearch import search

connection = pyodbc.connect('Driver={SQL Server};'
                            'Server=LAPTOP-IDQLUMAT\SQLSERVER;'
                            'Database=sameer;'
                            'Trusted_Connection=yes;')

cursor = connection.cursor()
rows = cursor.execute('SELECT * FROM [sameer].[dbo].nonzoning where update_status is null ').fetchall()

for row in rows:
    ds = row[0]
    state = row[1]
    dataset = ds + ' ' + ' ' + state + ' ' + 'US'
    print(dataset)
    for url in search(dataset, tld='com', stop=1):
        # print(ds+''+url)
        cursor.execute("UPDATE [sameer].[dbo].nonzoning SET url = ?,update_status=? WHERE Dataset = ?", url, 'yes', ds)
        print('update for' + ds)
        cursor.commit()
