import sqlite3

# Connect to database
conn = sqlite3.connect("dbnew.db")

# Create tables
conn.execute('''
CREATE TABLE IF NOT EXISTS users(
usid INTEGER PRIMARY KEY AUTOINCREMENT,
usnm TEXT,
pass TEXT
)
''')

conn.execute('''
CREATE TABLE IF NOT EXISTS new(
usid INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
address TEXT,
mobile TEXT
)
''')

# Insert data into users
conn.execute("INSERT INTO users(usnm, pass) VALUES ('Tae', 'vssi')")
conn.execute("INSERT INTO users(usnm, pass) VALUES ('Bhu', 'mie')")
conn.execute("INSERT INTO users(usnm, pass) VALUES ('kookie', 'jk')")

# Insert data into new
conn.execute("INSERT INTO new(name, address, mobile) VALUES ('Taehyung', 'Daegu', '010-2432-3245')")
conn.execute("INSERT INTO new(name, address, mobile) VALUES ('Jimin', 'Busan', '010-3210-3654')")
conn.execute("INSERT INTO new(name, address, mobile) VALUES ('Seokjin', 'Seoul', '010-3214-7610')")

conn.commit()

# Show data from both tables
print("Users Table:")
data = conn.execute("SELECT * FROM users")
for row in data:
    print(row)

print("\nNew Table:")
data = conn.execute("SELECT * FROM new")
for row in data:
    print(row)

# Update data
conn.execute("UPDATE users SET usnm = 'Bhumie' WHERE usid = 2")
conn.execute("UPDATE new SET name = 'Bhumie' WHERE usid = 2")
conn.commit()

# Delete data
uid = input("\nEnter ID to delete from users: ")
conn.execute("DELETE FROM users WHERE usid = " + uid)
conn.commit()

nid = input("Enter ID to delete from new: ")
conn.execute("DELETE FROM new WHERE usid = " + nid)
conn.commit()

# Final display
print("\nUsers Table After Delete:")
data = conn.execute("SELECT * FROM users")
for row in data:
    print(row)

print("\nNew Table After Delete:")
data = conn.execute("SELECT * FROM new")
for row in data:
    print(row)

conn.close()
