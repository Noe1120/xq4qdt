from fastapi import FastAPI, HTTPException
from database import db
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str

class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None

@app.get("/users")
async def get_users():
    users = db.execute_query("SELECT * FROM users")
    return [dict(user) for user in users]


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    users = db.execute_query(
        "SELECT * FROM users WHERE id = ?", 
        (user_id,)
    )
    if users:
        return dict(users[0])
    raise HTTPException(status_code=404, detail="用户不存在")

@app.post("/users")
async def create_user(user: UserCreate):
    try:
        user_id = db.execute_query(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user.name, user.email)
        )
        return {
            "message": "用户创建成功",
            "user_id": user_id,
            "data": {"name": user.name, "email": user.email}
        }
    except sqlite3.IntegrityError: # type: ignore
        raise HTTPException(status_code=400, detail="邮箱已存在")


@app.put("/users/{user_id}")
async def update_user(user_id: int, user: UserUpdate):
    existing = db.execute_query(
        "SELECT * FROM users WHERE id = ?", 
        (user_id,)
    )
    if not existing:
        raise HTTPException(status_code=404, detail="用户不存在")
    
    updates = []
    params = []
    
    if user.name:
        updates.append("name = ?")
        params.append(user.name)
    if user.email:
        updates.append("email = ?")
        params.append(user.email)
    
    if updates:
        params.append(user_id)
        query = f"UPDATE users SET {', '.join(updates)} WHERE id = ?"
        db.execute_query(query, tuple(params))
    
    return {"message": "用户更新成功"}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    result = db.execute_query(
        "DELETE FROM users WHERE id = ?", 
        (user_id,)
    )
    if result == 0:
        raise HTTPException(status_code=404, detail="用户不存在")
    return {"message": "用户删除成功"}