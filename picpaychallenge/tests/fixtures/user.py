from datetime import datetime
from secrets import token_hex
from typing import Dict, Union
from uuid import uuid4

from pytest import fixture
from pytz import utc

from picpaychallenge.src.entities.user import User, UserType

USER_DATA_TYPING = Dict[str, Union[datetime, str, UserType]]


@fixture
def valid_user_data() -> USER_DATA_TYPING:
    """Fixture for generating valid user data for testing purposes.

    Returns:
        USER_DATA_TYPING: A dictionary containing valid user data.
    """
    return {
        "id": str(uuid4()),
        "created_at": datetime.now(utc).isoformat(),
        "updated_at": datetime.now(utc).isoformat(),
        "name": token_hex(),
        "cpf": "123.456.789-09",
        "email": f"{token_hex(10)}@google.com",
        "password": "secure_password",
        "user_type": UserType.COMMON_USER,
    }


@fixture
def user(valid_user_data: USER_DATA_TYPING) -> User:
    """Fixture for creating a User object with valid data.

    Args:
        valid_user_data (dict): Valid user data.

    Returns:
        User: A User object with valid data.

    """
    return User(**valid_user_data)
