import sqlite3
import random
import datetime
from propan import PropanApp, RabbitBroker
from utils import initDB
from models.orders import OrdersDto, STATUS_IN_DELIVERY

# It's temporary
conn = sqlite3.connect('example.db')
broker = RabbitBroker("amqp://root:root@rabbitmq/")
app = PropanApp(broker)

initDB(conn)

random.seed(41)
    
@broker.handle("orders")
async def orders_handler(body: OrdersDto):
    db = sqlite3.connect('example.db')
    c = db.cursor()

    c.execute("SELECT * FROM users WHERE id = " + body.user + " LIMIT 1")
    user = c.fetchall()
    if len(user) == 0:
        print('There is no user ' + body.user + ' in db')
        return False

    user_id = user[0].id
    product_id = body.product
    code = random.randint(10000,99999)
    delivery_point_id = body.delivery

    c.execute("INSERT INTO orders (product, datetime, user, code, status, delivery_point) VALUES (?,?,?,?,?,?)", (
        product_id,
        datetime.datetime.now(),
        user_id,
        code,
        STATUS_IN_DELIVERY,
        delivery_point_id
    ))

    # Save (commit) the changes
    db.commit()

    c = db.cursor()
    c.execute("UPDATE users SET count_orders = count_orders + 1 WHERE id = " + user_id)
    db.commit()


