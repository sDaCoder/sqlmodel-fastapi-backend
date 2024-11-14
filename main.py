from fastapi import FastAPI
import uvicorn
from routes.greetUserRouter import greetUserRouter
from routes.addUserRouter import addUserRouter

app = FastAPI()

app.include_router(router = greetUserRouter)
app.include_router(router = addUserRouter)


# Starting the server
if __name__ == '__main__':
    uvicorn.run("main:app", host='localhost', port=80, reload=True)