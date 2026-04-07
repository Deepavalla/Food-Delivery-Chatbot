import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="chatbot"
)

cursor = conn.cursor()

def get_price(item):
    cursor.execute("SELECT price FROM food_items WHERE name=%s", (item,))
    result = cursor.fetchone()
    return result[0] if result else 0

def insert_order(item, qty, total):
    query = "INSERT INTO orders (item, quantity, total) VALUES (%s, %s, %s)"
    cursor.execute(query, (item, qty, total))
    conn.commit()
    return cursor.lastrowid

def track_order(order_id):
    cursor.execute("SELECT status FROM orders WHERE id=%s", (order_id,))
    result = cursor.fetchone()
    return result[0] if result else "Not found"
