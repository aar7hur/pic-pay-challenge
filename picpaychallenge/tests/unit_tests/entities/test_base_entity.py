from datetime import datetime
from secrets import token_hex
from uuid import uuid4

import pytest
import pytz

from picpaychallenge.src.entities.base_entity import BaseEntity


@pytest.fixture
def valid_uuid() -> str:
    """Fixture for providing a valid UUID.

    Returns:
        str: a valid uuid4 string
    """
    return str(uuid4())


@pytest.fixture
def valid_datetime() -> datetime:
    """Fixture for providing a valid datetime object.

    Returns:
        datetime: a valid datetime object"""
    return datetime.now(pytz.utc)


def test_validate_uuid_success(valid_uuid: str, valid_datetime: datetime) -> None:
    """Test the validation of a valid UUID in BaseEntity.

    Args:
        valid_uuid (str): A valid UUID.
        valid_datetime (datetime): A valid datetime object.

    Returns:
        None
    """
    # Arrange
    model_instance = BaseEntity(id=valid_uuid, created_at=valid_datetime, updated_at=valid_datetime)

    # Act
    id_value = model_instance.id

    # Assert
    assert id_value == valid_uuid


def test_validate_iso_datetime_success(valid_uuid: str, valid_datetime: datetime) -> None:
    """Test the validation of a valid datetime object in BaseEntity.

    Args:
        valid_uuid (str): A valid UUID.
        valid_datetime (datetime): A valid datetime object.

    Returns:
        None
    """
    # Arrange
    model_instance = BaseEntity(id=valid_uuid, created_at=valid_datetime, updated_at=valid_datetime)

    # Act
    created_at_value = model_instance.created_at
    updated_at_value = model_instance.updated_at

    # Assert
    assert created_at_value == valid_datetime
    assert updated_at_value == valid_datetime


def test_invalid_uuid_raises_error(valid_uuid: str) -> None:
    """Test that an invalid UUID raises a ValueError.

    Args:
        valid_uuid (str): A valid UUID.

    Returns:
        None
    """
    # Arrange & Act
    with pytest.raises(ValueError):
        BaseEntity(id=token_hex(), updated_at=datetime.now(), created_at=datetime.now())


def test_invalid_iso_datetime_raises_error(valid_uuid: str) -> None:
    """Test that an invalid datetime object raises a ValueError.

    Args:
        valid_uuid (str): A valid UUID.

    Returns:
        None
    """
    # Arrange & Act
    with pytest.raises(ValueError):
        BaseEntity(id=valid_uuid, updated_at=datetime.now(), created_at=token_hex())
