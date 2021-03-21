from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException

from fastapi import APIRouter

from app.auth.auth_manager import manager
from app.model.user_model import UserModel
router = APIRouter()
user_model = UserModel()
@router.post('/auth/token')
def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password

    user = user_model.get_user(username)  # we are using the same function to retrieve the user
    if not user:
        raise InvalidCredentialsException  # you can also use your own HTTPException
    elif password != user['password']:
        raise InvalidCredentialsException

    access_token = manager.create_access_token(
        data=dict(sub=username)
    )
    return {'access_token': access_token, 'token_type': 'bearer'}