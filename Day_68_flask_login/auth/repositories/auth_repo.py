from auth.DTO import UserDTO
from auth.models import User
from auth.extensions import auth_db as db
import sqlalchemy as sa
from sqlalchemy.exc import IntegrityError


def register(user: UserDTO) -> User | None:
    try:
        new_user = User(
            name=user.name,
            email=user.email,
            password=user.password
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user
    except IntegrityError as error:
        print(error)
        return None


def get_user(email: str) -> User | None:
    user: User = db.session.execute(sa.select(User).where(User.email == email)).scalar()
    return user
