from fastapi import FastAPI
from bson import ObjectId
from db import db
from models import User

app = FastAPI()

# convert _id to string
def fix_id(item):
    item["id"] = str(item["_id"])
    del item["_id"]
    return item


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/users/")
async def create_user(user: User):
    user_dict = user.dict()
    result = await db.users.insert_one(user_dict)
    return {"message":"user created successfully"}


@app.get("/users/")
async def get_users():
    users = await db.users.find().to_list(100)
    return [fix_id(item) for item in users]


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        return fix_id(user)
    else:
        return {"message": "User not found"}