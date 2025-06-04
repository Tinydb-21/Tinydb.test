from tinydb import TinyDB, Query
from collections import Counter
db = TinyDB('db.json')
users_table = db.table('users')
products_table = db.table('products')
orders_table = db.table('orders')
users_table.insert_multiple([
    {'name': 'Alice', 'age': 22, 'email': 'alice@example.com', 'active': True},
    {'name': 'Bob', 'age': 30, 'email': 'bob@example.com', 'active': False},
    {'name': 'Charlie', 'age': 25, 'email': 'charlie@example.com', 'active': True}
])
products_table.insert_multiple([
    {'product_id': 1, 'name': 'Laptop', 'price': 1200, 'stock': 5},
    {'product_id': 2, 'name': 'Phone', 'price': 800, 'stock': 10}
])
orders_table.insert_multiple([
    {'order_id': 1, 'user_name': 'Alice', 'product_id': 1, 'quantity': 1, 'status': 'completed'},
    {'order_id': 2, 'user_name': 'Bob', 'product_id': 2, 'quantity': 2, 'status': 'pending'},
    {'order_id': 3, 'user_name': 'Alice', 'product_id': 2, 'quantity': 1, 'status': 'completed'}
])
User = Query()
active_users = users_table.search(User.active == True)
Product = Query()
expensive_products = products_table.search(Product.price > 1000)
Order = Query()
alice_orders = orders_table.search(Order.user_name == 'Alice')
order_counts = Counter([o['user_name'] for o in orders_table.all()])
def get_order_details():
    details = []
    for order in orders_table.all():
        user = users_table.get(Query().name == order['user_name'])
        product = products_table.get(Query().product_id == order['product_id'])
        details.append({
            'order_id': order['order_id'],
            'user': user['name'] if user else None,
            'product': product['name'] if product else None,
            'quantity': order['quantity'],
            'status': order['status'],
            'user_email': user['email'] if user else None,
            'product_price': product['price'] if product else None
        })
    return details
users_table.update({'active': True}, User.name == 'Bob')
orders_table.update({'status': 'completed'}, (Order.user_name == 'Bob') & (Order.status == 'pending'))
users_table.remove(User.name == 'Charlie')
orders_table.remove(Order.status == 'completed')
print("All users:", users_table.all())
print("Active users:", active_users)
print("All products:", products_table.all())
print("Expensive products:", expensive_products)
print("All orders:", orders_table.all())
print("Alice's orders:", alice_orders)
print("Order counts per user:", dict(order_counts))
print("Order details:", get_order_details())
