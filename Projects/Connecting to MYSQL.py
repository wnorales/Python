import mysql.connector


Database = mysql.connector.connect(user='wnorales', password='Norales22#', host='localhost', database='sys',  auth_plugin='mysql_native_password')
Database.close