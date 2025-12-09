from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

# -------------------------------
# In-Memory Users API
# -------------------------------
users_db = [
    {"id": 1, "name": "Rahul", "age": 25},
    {"id": 2, "name": "Aisha", "age": 22},
]

class UserCreate(BaseModel):
    name: str
    age: int

@app.get("/")
def read_root():
    return {"message": "Kunal's API running successfully!"}

@app.get("/users")
def get_users():
    return {"users": users_db}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}

@app.post("/users")
def create_user(user: UserCreate):
    new_id = len(users_db) + 1
    new_user = {"id": new_id, "name": user.name, "age": user.age}
    users_db.append(new_user)
    return new_user


# -------------------------------
# Excel → JSON API
# -------------------------------
@app.get("/excel-data")
def get_excel_data():
    df = pd.read_excel("users.xlsx")   # file should exist in project folder
    data = df.to_dict(orient="records")  # Convert to JSON list
    return {"data": data}
