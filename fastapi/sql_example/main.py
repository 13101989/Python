from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import User, get_db
from pydantic import BaseModel

app = FastAPI()


@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


class UserBody(BaseModel):
    name: str
    email: str


@app.post("/user")
def add_new_user(user: UserBody, db: Session = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@app.get("/user/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@app.put("/user/{user_id}")
def update_user(user_id: int, user: UserBody, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.name = user.name
    db_user.email = user.email

    db.commit()
    db.refresh(db_user)

    return db_user


@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()

    return {"detail": "User deleted"}
