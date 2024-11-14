from fastapi import APIRouter
from controllers.greet import greet

greetUserRouter = APIRouter()

@greetUserRouter.get('/')
def root():
    return greet()