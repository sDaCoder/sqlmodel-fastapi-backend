from fastapi import UploadFile, File
from schemas.userSchema import userSchema
from sqlmodel import Session
from sqlalchemy.exc import IntegrityError
from connectDB import connect
import datetime
import shutil
from pathlib import Path

DB: str = "database.db"
sqlite_url: str = f"sqlite:///{DB}"
engine = connect(sqlite_url)

def add_user(name: str, email: str, age: int, image: UploadFile = File(...)):

    # Uploading the file
    UPLOAD_DIR = f"./uploads/{email}"
    Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
    file_location = f"{UPLOAD_DIR}/{image.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    # Attaching the date and time with the DB
    x = datetime.datetime.now()
    date = str(x).split(" ")[0]
    time = str(x).split(" ")[1].split(".")[0]

    # Adding the user
    new_user = userSchema(name=name, email=email, age=age, date=date, time=time, img_location = file_location)
    with Session(engine) as session:
        session.add(new_user)
        try:
            session.commit()
            session.refresh(new_user)
            return {
                "status": "Success",
                "message": "User Added",
                "User": new_user
            }
        except IntegrityError:
            session.rollback()
            return {
                "status": "Failed",
                "message": "Duplicate data found",
            }