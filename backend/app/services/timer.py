from time import time

from sqlalchemy.orm.session import Session
from app import models, schemas
from app.errors import InvalidCredentialsError, TimerNotFoundError
from app.repository.timer import TimerRespository


def create_timer(
    user_id: int, request: schemas.TimerCreateIn, session: Session
) -> models.Timer:
    new_timer = models.Timer(
        user_id=user_id,
        created_at=time(),
        title=request.title,
        time=request.time,
    )
    try:
        TimerRespository(session).save(new_timer)
    except Exception:
        raise Exception
    return new_timer


def __is_timer_owner(timer_id: int, user_id: int, session: Session) -> bool:
    user_timers = TimerRespository(session).get_all(user_id)
    return timer_id in [user_timer.id for user_timer in user_timers]


def get_timer(session: Session, user_id: int, timer_id: int) -> list[models.Timer]:
    """Creates and stores a new user in a database

    :param request: The request body for users to input their new account credentials
    :type: schemas.UserIn
    :param session: The database that user's credentials are uploaded to
    :type session: Session
    :returns: Full details of the created user
    :rtype: models.User
    raises UsernameNotUniqueError: if username in request.username is already taken
    in the session database
    """

    if not __is_timer_owner(timer_id, user_id, session):
        raise InvalidCredentialsError
    try:
        timer = TimerRespository(session).get(timer_id)
        return timer
    except TimerNotFoundError:
        raise TimerNotFoundError


def get_all_timers(user_id: int, session: Session) -> list[models.Timer]:
    """Creates and stores a new user in a database

    :param request: The request body for users to input their new account credentials
    :type: schemas.UserIn
    :param session: The database that user's credentials are uploaded to
    :type session: Session
    :returns: Full details of the created user
    :rtype: models.User
    raises UsernameNotUniqueError: if username in request.username is already taken
    in the session database
    """

    try:
        timer = TimerRespository(session).get_all(user_id)
        return timer
    except TimerNotFoundError:
        raise TimerNotFoundError


def delete_timer(timer_id: int, user_id: int, session: Session) -> None:
    if not __is_timer_owner(timer_id, user_id, session):
        raise InvalidCredentialsError

    try:
        return TimerRespository(session).delete(timer_id)
    except TimerNotFoundError:
        raise TimerNotFoundError
