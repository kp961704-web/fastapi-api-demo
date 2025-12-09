from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Dummy in-memory database
users_db = [
    {"id": 1, "name": "Rahul", "age": 25},
    {"id": 2, "name": "Aisha", "age": 22},
]

# Request body ke liye model
class UserCreate(BaseModel):
    name: str
    age: int


@app.get("/")
def read_root():
    return {"message": "User API running successfully!"}


# 1) Saare users laane ka endpoint
@app.get("/users")
def get_users():
    return {"users": users_db}


# 2) Specific user by id
@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}


# 3) Naya user create karne ka endpoint (POST)
@app.post("/users")
def create_user(user: UserCreate):
    new_id = len(users_db) + 1
    new_user = {"id": new_id, "name": user.name, "age": user.age}
    users_db.append(new_user)
    return new_user
