from sqlalchemy.orm import Session
import models
import schemas


# Create a new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.Users(
        name=user.name,
        email=user.email,
        age=user.age
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


# Get all users
def get_users(db: Session):
    return db.query(models.Users).all()


# Get a user by ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()


# Update a user
def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.Users).filter(models.Users.id == user_id).first()

    if not db_user:
        return None

    if user.name is not None:
        db_user.name = user.name

    if user.email is not None:
        db_user.email = user.email

    if user.age is not None:
        db_user.age = user.age

    db.commit()
    db.refresh(db_user)

    return db_user


# Delete a user
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.Users).filter(models.Users.id == user_id).first()

    if not db_user:
        return None

    db.delete(db_user)
    db.commit()

    return db_user