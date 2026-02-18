from database import db

db.execute_query(
    "INSERT INTO users (name, email) VALUES (?, ?)",
    ("测试用户", "test@example.com")
)

users = db.execute_query("SELECT * FROM users")
for user in users:
    print(dict(user))