from sqlalchemy.orm import Session

import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.User):
    db_user = models.User(name=user.name, image=user.image)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print(db_user.id)
    return db_user


def update_user(db: Session, user: schemas.User):
    db_user = db.query(models.User).filter(models.User.id == user.id).first()
    db_user.image = user.image
    db.commit()
    db.refresh(db_user)
    return db_user
