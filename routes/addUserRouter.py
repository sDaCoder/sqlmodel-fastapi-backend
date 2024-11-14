from fastapi import APIRouter, UploadFile, File, Form
from controllers.addUser import add_user

addUserRouter = APIRouter()

@addUserRouter.post("/")
def postRoot(
    name: str = Form(...), 
    email: str = Form(...), 
    age: int = Form(...),
    image: UploadFile = File(...)
):
    return add_user(name = name, email = email, age = age, image = image)