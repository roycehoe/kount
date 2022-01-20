from sqlalchemy.exc import IntegrityError, InvalidRequestError
from sqlalchemy.orm.session import Session

from app import models
from app.errors import TimerNotFoundError


class TimerRespository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, timer: models.Timer) -> models.Timer:
        try:
            self.session.add(timer)
            self.session.commit()
            return timer

        except IntegrityError:
            pass

    def get(self, timer_id: int) -> models.Timer:
        if timer := (
            self.session.query(models.Timer).filter(models.Timer.id == timer_id).first()
        ):
            return timer
        raise TimerNotFoundError

    def get_all(self, user_id: str) -> list[models.Timer]:
        if timer := (
            self.session.query(models.Timer).filter(models.Timer.user_id == user_id)
        ).all():
            return timer
        raise TimerNotFoundError

    def delete(self, timer_id: int) -> None:
        if timer := self.session.query(models.Timer).filter(
            models.Timer.id == timer_id
        ):
            timer.delete()
            self.session.commit()
            return
        raise TimerNotFoundError
