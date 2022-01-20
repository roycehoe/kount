from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import schemas
from app.database import get_session
from app.errors import USERNAME_TAKEN, UsernameNotUniqueError
from app.services import user

router = APIRouter(tags=["hello_world"], prefix="/hello_world")


@router.get(
    "",
    status_code=status.HTTP_200_OK,
)
def hello_world():
    """Creates and stores a new user in a database

    :param request: The request body for users to input their new account credentials
    :type: schemas.UserIn
    :param session: The database that user's credentials are uploaded to
    :type session: Session
    :returns: The user's username
    :rtype: schemas.UserOut
    :raises HTTPException: If username validation fails
    """
    return "hello world"
