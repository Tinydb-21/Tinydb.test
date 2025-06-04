from tinydb import TinyDB, Query
import json

# Node A
db_a = TinyDB('node_a.json')
# Node B
db_b = TinyDB('node_b.json')

User = Query()

def sync_data(source_db, target_db):
    # Lấy toàn bộ dữ liệu từ source_db
    all_data = source_db.all()
    # Xóa dữ liệu cũ target_db để đồng bộ
    target_db.truncate()
    # Chèn lại toàn bộ dữ liệu từ source_db
    for item in all_data:
        target_db.insert(item)

# Node A thêm dữ liệu
db_a.insert({'id': 1, 'name': 'Alice', 'score': 90})

# Đồng bộ từ Node A sang Node B
sync_data(db_a, db_b)

print("Dữ liệu Node A:", db_a.all())
print("Dữ liệu Node B sau sync:", db_b.all())

# Node B cập nhật thêm dữ liệu
db_b.insert({'id': 2, 'name': 'Bob', 'score': 85})

# Đồng bộ ngược lại từ B sang A
sync_data(db_b, db_a)

print("Dữ liệu Node A sau sync ngược:", db_a.all())
