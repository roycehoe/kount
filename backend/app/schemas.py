from fastapi.exceptions import HTTPException
from pydantic import BaseModel, Field, validator
from pydantic.types import SecretStr
from starlette import status

from app.errors import INVALID_TIMER_LENGTH_ERROR


class UserIn(BaseModel):
    """A request body to create users

    :param username: The new user's username
    :type username: str, max_length=128
    :param password: The new user's password
    :type password: str, max_length=128
    """

    username: str = Field(max_length=128)
    password: str = Field(max_length=128)


class UserOut(BaseModel):
    """A response body after users have been successfully created

    :param username: The new user's username
    :type username: str
    """

    username: str

    class Config:
        orm_mode = True


class TokenOut(BaseModel):
    """A respose body for a successfully created JWT token

    :param access_token: The JWT access token
    :type access_token: str
    :param token_type: A description of the token type
    :type token_type: str
    """

    access_token: str
    token_type: str


class LoginIn(BaseModel):
    """A request body for users to key in their credentials

    :param username: The user's username
    :type username: SecretStr
    :param password: The user's password
    :type password: SecretStr
    """

    username: SecretStr = Field(max_length=128)
    password: SecretStr = Field(max_length=128)


class TimerCreateIn(BaseModel):
    title: str
    time: int

    @validator("time", pre=True)
    def invalid_time(cls, time):
        if time < 1 or time > 86400:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail={
                    "error": INVALID_TIMER_LENGTH_ERROR,
                },
            )

        return time


class TimerOut(BaseModel):
    id: int
    created_at: float
    title: str
    time: int

    class Config:
        orm_mode = True


class TimerGetIn(BaseModel):
    user_id: int


class TimerDeleteIn(BaseModel):
    timer_id: int
