import sqlite3 as sql

#Create and connect, create cursor, apply query, commit changes to db, close connection



def create_table():
    # Automatically creates db if doesnt exist
    conn = sql.connect("app.db")
    cursor = conn.cursor()
    # Pass sql query
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, qty, price):
    conn = sql.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO store VALUES (?, ?, ?)", (item, qty, price))
    conn.commit()
    conn.close()


# insert("Wine", 10, 123.23)

def view():
    conn = sql.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sql.connect("app.db")
    cursor = conn.cursor()
    # CRITICAL ','
    cursor.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    conn.close()


def update(item, qty, price):
    conn = sql.connect("app.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity = ?, price = ? WHERE item= ?", (qty,price, item))
    conn.commit()
    conn.close()

# delete("Wine")
print(view())
update("IPhone", 20, 40002)
print(view())
