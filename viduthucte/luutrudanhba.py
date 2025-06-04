from tinydb import TinyDB, Query

# Khởi tạo cơ sở dữ liệu và xóa dữ liệu cũ
db = TinyDB('contacts.json')
db.truncate()

# Thêm dữ liệu
db.insert({'name': 'Alice', 'phone': '123-4567', 'email': 'alice@example.com'})
db.insert({'name': 'Bob', 'phone': '987-6543', 'email': 'bob@example.com'})
db.insert({'name': 'Charlie', 'phone': '555-1234', 'city': 'New York'})  # Charlie không có email

# Truy vấn dữ liệu
Contact = Query()
alice_contacts = db.search(Contact.name == 'Alice')  # Tìm liên hệ của Alice
contacts_with_email = db.search(Contact.email.exists())  # Tìm liên hệ có email
contacts_with_phone_prefix = db.search(Contact.phone.matches('^123'))  # SĐT bắt đầu bằng '123'

# Cập nhật dữ liệu: thay đổi số điện thoại của Alice
db.update({'phone': '111-2222'}, Contact.name == 'Alice')

# Xóa Bob khỏi danh bạ
db.remove(Contact.name == 'Bob')

# Đóng cơ sở dữ liệu
db.close()
