import psycopg2 as sql

def create_table():
    conn = sql.connect("dbname = 'database1' user='yashrtiwari' password='yash1234' host='localhost' port ='5432' ")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, qty, price):
    conn = sql.connect("dbname = 'database1' user='yashrtiwari' password='yash1234' host='localhost' port ='5432' ")
    cursor = conn.cursor()
    # cursor.execute("INSERT INTO store VALUES (?, ?, ?)", (item, qty, price))
    cursor.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, qty, price))
    conn.commit()
    conn.close()

def view():
    conn = sql.connect("dbname = 'database1' user='yashrtiwari' password='yash1234' host='localhost' port ='5432' ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sql.connect("dbname = 'database1' user='yashrtiwari' password='yash1234' host='localhost' port ='5432' ")
    cursor = conn.cursor()
    # CRITICAL ','
    cursor.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    conn.close()

def update(item, qty, price):
    conn = sql.connect("dbname = 'database1' user='yashrtiwari' password='yash1234' host='localhost' port ='5432' ")
    cursor = conn.cursor()
    cursor.execute("UPDATE store SET quantity = ?, price = ? WHERE item= ?", (qty,price, item))
    conn.commit()
    conn.close()

create_table()

insert("M30", 1, 15000)
