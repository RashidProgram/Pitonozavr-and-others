# !/usr/bin/env python3
import cgi
import sqllite3


f = cgi.FieldStorage().getvalue("username")
q = cgi.FieldStorage().getvalue("password")

db = sqllite3.connect("account.db")
coursor = db.cursor()


coursor.execute("""CREATE TABLE """)

print("Content-type: text/html")
print()
print(q)




