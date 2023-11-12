from enum import Enum, auto
from typing import Union

from pydantic import SecretStr, field_validator

# from email_validator import validate_email
from picpaychallenge.src.entities.base_entity import BaseEntity


class UserType(Enum):
    """Enumeration representing different user types."""

    COMMON_USER = auto()
    RETAILER = auto()


class User(BaseEntity):
    """Represents the user entity."""

    name: str
    cpf: str
    email: str  # EmailStr from pydantic seems not working
    password: SecretStr
    user_type: Union[UserType, str]

    @field_validator("email")
    @classmethod
    def validate_email(cls, value: str) -> str:
        """Validate and format the email input.

        Args:
            value (str): The email input.

        Returns:
            str: The formatted email.

        """
        # @TODO: email = validate_email(value)
        # return email.normalized
        return value

    @field_validator("cpf")
    @classmethod
    def validate_cpf(cls, value: str) -> str:
        """Validate and format the CPF input.

        Args:
            value (str): The CPF input.

        Returns:
            str: The formatted CPF.

        """
        # @TODO: add cpf validator.
        return value

    @field_validator("user_type")
    @classmethod
    def user_type_must_belongs_to_enum(cls, value: str) -> UserType:
        """Validate and convert the user type to UserType enum.

        Args:
            value (str): The user type input.

        Returns:
            UserType: The converted UserType enum.

        Raises:
            ValueError: If the user type is invalid.
        """
        try:
            return UserType(value)
        except ValueError:
            raise ValueError("Invalid user type.")
