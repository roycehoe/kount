from typing import List
from urllib import response
from fastapi import APIRouter, Depends, HTTPException, status, Header
from jose.exceptions import JWTError
from sqlalchemy.orm import Session

from app import schemas
from app.database import get_session
from app.errors import (
    INVALID_CREDENTIALS,
    TIMER_NOT_FOUND_ERROR,
    TOKEN_AUTHENTICATION_FAILED,
    USERNAME_TAKEN,
    InvalidAuthenticationTokenError,
    InvalidCredentialsError,
    MissingAuthenticationTokenError,
    TimerNotFoundError,
    UsernameNotUniqueError,
)
from app.models import Timer

from app.services import timer
from app.token import get_user_id

router = APIRouter(tags=["timer"], prefix="/timer")


@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.TimerOut)
def create_timer(
    request: schemas.TimerCreateIn,
    token: str = Header(None),
    session: Session = Depends(get_session),
):
    """Creates and stores a new user in a database

    :param request: The request body for users to input their new account credentials
    :type: schemas.UserIn
    :param session: The database that user's credentials are uploaded to
    :type session: Session
    :returns: The user's username
    :rtype: schemas.UserOut
    :raises HTTPException: If username validation fails
    """
    try:
        user_id = get_user_id(token)
    except MissingAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": MissingAuthenticationTokenError},
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )
    except InvalidAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )

    try:
        return timer.create_timer(user_id, request, session)

    except UsernameNotUniqueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": USERNAME_TAKEN},
        )


@router.get("", status_code=status.HTTP_200_OK, response_model=List[schemas.TimerOut])
def get_timer(token: str = Header(None), session: Session = Depends(get_session)):
    """Creates and stores a new user in a database

    :param request: The request body for users to input their new account credentials
    :type: schemas.UserIn
    :param session: The database that user's credentials are uploaded to
    :type session: Session
    :returns: The user's username
    :rtype: schemas.UserOut
    :raises HTTPException: If username validation fails
    """
    try:
        user_id = get_user_id(token)
    except MissingAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": MissingAuthenticationTokenError},
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )
    except InvalidAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )

    try:
        return timer.get_all_timers(user_id, session)
    except TimerNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": TIMER_NOT_FOUND_ERROR},
        )


@router.get(
    "/{timer_id}", status_code=status.HTTP_200_OK, response_model=schemas.TimerOut
)
def get_timer(
    timer_id: int, token: str = Header(None), session: Session = Depends(get_session)
):
    """Creates and stores a new user in a database

    :param request: The request body for users to input their new account credentials
    :type: schemas.UserIn
    :param session: The database that user's credentials are uploaded to
    :type session: Session
    :returns: The user's username
    :rtype: schemas.UserOut
    :raises HTTPException: If username validation fails
    """
    try:
        user_id = get_user_id(token)
    except MissingAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": MissingAuthenticationTokenError},
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )
    except InvalidAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )

    try:
        return timer.get_timer(session, user_id, timer_id)
    except TimerNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": TIMER_NOT_FOUND_ERROR},
        )
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": INVALID_CREDENTIALS},
        )


@router.delete("", status_code=status.HTTP_200_OK, response_model=None)
def delete_timer(
    request: schemas.TimerDeleteIn,
    token: str = Header(None),
    session: Session = Depends(get_session),
):
    """Creates and stores a new user in a database

    :param request: The request body for users to input their new account credentials
    :type: schemas.UserIn
    :param session: The database that user's credentials are uploaded to
    :type session: Session
    :returns: The user's username
    :rtype: schemas.UserOut
    :raises HTTPException: If username validation fails
    """
    try:
        user_id = get_user_id(token)
    except MissingAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": MissingAuthenticationTokenError},
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )
    except InvalidAuthenticationTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": TOKEN_AUTHENTICATION_FAILED},
        )

    try:
        return timer.delete_timer(request.timer_id, user_id, session)
    except TimerNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={"error": TIMER_NOT_FOUND_ERROR},
        )
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={"error": INVALID_CREDENTIALS},
        )
