from fastapi import FastAPI
from routes.user import user
app = FastAPI(
    title = "REST API with FastAPI and Mongodb",
    description = "This is a simple REST API",
    version = "0.0.1"
)

app.include_router(user)