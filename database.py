import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="*******",
    database="testdb",
)

# print(mydb)

my_cursor = mydb.cursor()
# mydb.cursor is just a instance of actual cursor

# create db
my_cursor.execute("CREATE DATABASE testdb")


# show db
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

# creating table
my_cursor.execute(
    "CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")


# showing tables
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table[0])


# inserting into db
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
record1 = ("John", "john@codemy.com", 40)

my_cursor.execute(sqlStuff, record1)
mydb.commit()


# inserting many records
sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
records = [
    ("Johnny", "johnny@codemy.com", 41),
    ("Johnathon", "johnathon@codemy.com", 36),
    ("Joma", "joma@codemy.com", 45),
]

my_cursor.executemany(sqlStuff, records)
mydb.commit()


# showing data
my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()
for row in  result:
    print(row)
    # print(row[1])

#  Pull Data from the table
my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()
print("NAME\tEMAIL\t\t\tAGE\tID")
print("----\t-----\t\t\t---\t---")
for row in result:
    print(row[0] + "\t%s" %row[1]+ "\t\t%s" %row[2]+ "\t%s" %row[3])


# where clause
my_cursor.execute("SELECT * FROM users WHERE  name = 'john'")
result = my_cursor.fetchall()
for row in result:
    print(row)


# where like and wildcards
my_cursor.execute("SELECT * FROM users WHERE  name LIKE 'j%'")
result = my_cursor.fetchall()
for row in result:
    print(row)


# AND / OR clause
my_cursor.execute("SELECT * FROM users WHERE  name LIKE 'j%' AND age>40")
result = my_cursor.fetchall()
for row in result:
    print(row)


# Updating record
my_sql = "UPDATE users SET age = 17 WHERE user_id = 3"
my_cursor.execute(my_sql)
mydb.commit()

# Limiting the results
my_cursor.execute("SELECT * FROM users LIMIT 2 OFFSET 1")
result = my_cursor.fetchall()
for row in result:
    print(row)


# Order by
my_cursor.execute("SELECT * FROM users ORDER BY age ASC")
result = my_cursor.fetchall()
for row in result:
    print(row)


# DELETE record
my_sql = "DELETE FROM users WHERE user_id = 1"
my_cursor.execute(my_sql)
mydb.commit()

# DELETE / DROP table
my_sql = "DROP TABLE  IF EXISTS users"
my_cursor.execute(my_sql)
