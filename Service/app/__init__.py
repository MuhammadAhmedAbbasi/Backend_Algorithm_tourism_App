from fastapi import FastAPI
from .app import router as non_login_router
from .login_app import router as login_router 
from .beautification_app import router as beautification_router 
from .caption_app import router as caption_router
from .description_app import router as description_router
from .video_app import router as video_router
from config import BASE_API_URL  # Import from config.py

def create_app():
    app = FastAPI()
    return app

def register_router(app: FastAPI):
    app.include_router(router=non_login_router, prefix=BASE_API_URL)
    app.include_router(router=login_router, prefix=BASE_API_URL)
    app.include_router(router=beautification_router, prefix=BASE_API_URL)
    app.include_router(router=caption_router, prefix=BASE_API_URL)
    app.include_router(router=description_router, prefix=BASE_API_URL)
    app.include_router(router=video_router, prefix=BASE_API_URL)