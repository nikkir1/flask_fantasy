def initDB(conn):
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS orders
                 (id integer, product integer, datetime text, user real, code integer, status integer, delivery_point integer)''')
    c.execute('''CREATE TABLE IF NOT EXISTS users
                     (id integer, name string, count_orders int)''')

    conn.commit()
