from database import user_collection
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, field_validator
from bson import ObjectId

app = FastAPI()


class Tweet(BaseModel):
    content: str
    hashtags: list[str]


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    tweets: list[Tweet] | None = None

    @field_validator("age")
    def validate_age(cls, value):
        if value < 18 or value > 100:
            raise ValueError("Age must be between 18 and 100")

        return value


class UserResponse(UserCreate):
    id: str


@app.get("/users")
def read_users():
    return [{**user, "_id": str(user["_id"])} for user in user_collection.find()]


@app.post("/user")
def create_user(user: UserCreate):
    result = user_collection.insert_one(user.model_dump(exclude_none=True))
    user_response = UserResponse(id=str(result.inserted_id), **user.model_dump())

    return user_response


@app.get("/user/{user_id}")
def get_user(user_id: str) -> UserResponse:
    db_user = user_collection.find_one(
        {"_id": ObjectId(user_id) if ObjectId.is_valid(user_id) else None}
    )

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # user_response = UserResponse(id=str(db_user["_id"]), **db_user)
    db_user["id"] = str(db_user["_id"])

    return db_user
