from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import UserResponse,UserCreate,UserUpdate
import crud

# import Users from 

router=APIRouter(
     prefix="/users",
     tags=["Users"]
)

@router.post("/", response_model=UserResponse)
def create_user(user:UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.get("/", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.get("/{id}")
def get_user_id(user_id: int,db: Session = Depends(get_db)):
        user = crud.get_user_by_id(db,user_id)
    
        if  user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        return user

@router.put("/{id}",response_model=UserResponse )
def update_users(user_id: int, user: UserUpdate, db: Session = Depends(get_db) ):
    updated_user = crud.update_user(db, user_id, user)

    if updated_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return updated_user

@router.delete("/{id}")
def delete_user_id(user_id: int,db: Session = Depends(get_db)):
        user = crud.delete_user(db,user_id)
    
        if  user is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        return user