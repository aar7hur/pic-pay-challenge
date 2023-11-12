from datetime import datetime
from typing import Union
from uuid import UUID, uuid4

import pytz
from pydantic import BaseModel, ValidationError, field_validator


class BaseEntity(BaseModel):
    """Represents the user entity."""

    id: str = str(uuid4())
    created_at: datetime = datetime.now(pytz.utc)
    updated_at: datetime = datetime.now(pytz.utc)

    @field_validator("id")
    @classmethod
    def validate_uuid(cls, value: str) -> str:
        """Validate and convert the input string to a UUID.

        Args:
            value (str): The input string representing a UUID.

        Returns:
            str: The string representation of the validated UUID.

        Raises:
            ValueError: If the input string is not a valid UUID.
        """
        try:
            uuid_obj = UUID(value, version=4)  # Change 'version' as needed
        except ValidationError as error:
            raise ValueError from error
        return str(uuid_obj)

    @field_validator("created_at", "updated_at", mode="before")
    @classmethod
    def validate_iso_datetime(cls, value: Union[str, datetime]) -> datetime:
        """Validate and convert the input string to a datetime object.

        Args:
            value (str): The input string representing an ISO 8601 formatted datetime.

        Returns:
            datetime: The datetime object representing the validated ISO 8601 datetime.

        Raises:
            ValueError: If the input string is not a valid ISO 8601 datetime.
        """
        if isinstance(value, datetime):
            return value.replace(tzinfo=pytz.utc)
        try:
            datetime_obj = datetime.fromisoformat(value).replace(tzinfo=pytz.utc)
        except (ValueError, ValidationError) as error:
            raise ValueError from error
        return datetime_obj
