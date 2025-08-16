# add this to main file
from fastapi import FastAPI
from response_feature import router as response_router

app = FastAPI()
app.include_router(response_router, prefix="/response")
