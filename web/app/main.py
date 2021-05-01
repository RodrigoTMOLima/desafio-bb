from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import engine, get_db
from utils import is_valid_image


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post(
    "/add-user",
    response_model=schemas.User,
    response_model_exclude={'name', 'image'},
)
def add_user(user: schemas.UserCreate, db: Session = Depends(get_db)): 
    if not is_valid_image(user.image):
        raise HTTPException(status_code=422, detail="Invalid image data")
    return crud.create_user(db=db, user=user)


@app.get(
    "/get-user-image/{user_id}",
    response_model=schemas.User,
    response_model_exclude={'id'},
)
def get_user_image(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.patch(
    "/update-user-image",
    response_model=schemas.User,
    response_model_exclude={'name'},
)
def update_user_image(user: schemas.UserUpdate, db: Session = Depends(get_db)): 
    db_user = crud.get_user(db, user_id=user.id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")  
    if not is_valid_image(user.image):  
        raise HTTPException(status_code=422, detail="Invalid image data")
    return crud.update_user(db=db, user=user)
