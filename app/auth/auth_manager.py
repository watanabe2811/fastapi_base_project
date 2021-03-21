from datetime import datetime

from fastapi_login import LoginManager
import app.config as config
from app.model.user_model import UserModel

SECRET = config.SECRET
manager = LoginManager(SECRET, tokenUrl='/auth/token')
user_model = UserModel()


@manager.user_loader
def get_user(username: str):
    print("run get user")
    return {
        'username': username,
        'request_time' : datetime.now()
    }