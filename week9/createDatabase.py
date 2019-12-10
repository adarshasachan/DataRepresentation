import mysql.connector

db = mysql.connector.connect(
  host="localhost`",
  user="root",
  password="Jump18joy"
  #user="datarep",  # this is the user name on my mac
  #passwd="Jump18joy" # for my mac
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE datarepresentation")