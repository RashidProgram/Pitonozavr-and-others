from peewee import *

db = MySQLDatabase("mydb", user = "root", passwd="123456")

class Book(Model):
	author = CharField()
	title = TextField()

	class Meta:
		database = db


#Book.create_table()
book = Book(author = "me", title = "peewee is coll")
book.save()
book = Book(author = "you", title = "Mysql is True")
book.save()
for book in Book.filter(author="me"):
	print(book.title)
	print(book.id)
		