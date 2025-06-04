from tinydb import TinyDB, Query
from datetime import datetime

class TaskManager:
    def __init__(self, db_path='tasks.json'):
        self.db = TinyDB(db_path)
        self.Task = Query()

    def add_task(self, description, due_date=None, completed=False):
        # Thêm một tác vụ mới
        task = {
            'description': description,
            'created_at': datetime.now().isoformat(),
            'due_date': due_date,
            'completed': completed
        }
        self.db.insert(task)

    def get_all_tasks(self):
        return self.db.all()

    def get_pending_tasks(self):
        return self.db.search(self.Task.completed == False)

    def mark_task_complete(self, description):
        # Đánh dấu hoàn thành
        self.db.update({'completed': True}, self.Task.description == description)

    def delete_task(self, description):
        self.db.remove(self.Task.description == description)

    def close(self):
        self.db.close()

if __name__ == "__main__":
    tm = TaskManager()
    tm.db.truncate()  # Xóa dữ liệu cũ

    # Thêm tác vụ mới
    tm.add_task("Mua sữa", "2025-05-29")
    tm.add_task("Viết báo cáo TinyDB")
    tm.add_task("Gọi cho khách hàng", "2025-05-30")

    all_tasks = tm.get_all_tasks()  # Lấy tất cả tác vụ
    pending_tasks = tm.get_pending_tasks()  # Tác vụ chưa hoàn thành

    tm.mark_task_complete("Mua sữa")  # Đánh dấu hoàn thành

    pending_after_done = tm.get_pending_tasks()  # Cập nhật danh sách chờ

    tm.delete_task("Gọi cho khách hàng")  # Xóa tác vụ

    remaining_tasks = tm.get_all_tasks()  # Tác vụ còn lại

    tm.close()
