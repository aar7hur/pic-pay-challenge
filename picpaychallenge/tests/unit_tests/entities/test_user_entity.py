from datetime import datetime

from picpaychallenge.src.entities.user import User
from picpaychallenge.tests.fixtures.user import USER_DATA_TYPING


def test_valid_user_data_creation(valid_user_data: USER_DATA_TYPING) -> None:
    """Test the creation of a User instance with valid user data.

    Args:
        valid_user_data (USER_DATA_TYPING): Valid user data.
    """
    # Arrange & Act
    user_instance = User(**valid_user_data)

    # Assert
    assert user_instance.id == valid_user_data["id"]
    assert user_instance.created_at == datetime.fromisoformat(valid_user_data["created_at"])
    assert user_instance.updated_at == datetime.fromisoformat(valid_user_data["updated_at"])
    assert user_instance.name == valid_user_data["name"]
    assert user_instance.cpf == valid_user_data["cpf"]
    assert user_instance.email == valid_user_data["email"]
    assert user_instance.password.get_secret_value() == valid_user_data["password"]
    assert user_instance.user_type == valid_user_data["user_type"]


# def test_valid_email_creation(valid_user_data: dict):
#     # Arrange
#     valid_email_user_data = valid_user_data.copy()

#     # Act
#     valid_email_user_data["email"] = "new.email@google.com"
#     user_instance = User(**valid_email_user_data)

#     # Assert
#     assert user_instance.email == valid_email_user_data["email"]


# def test_invalid_email_raises_error(valid_user_data: dict):
#     # Arrange
#     invalid_email_user_data = valid_user_data.copy()
#     invalid_email_user_data["email"] = token_hex()

#     # Act & Assert
#     with pytest.raises(ValueError):
#         User(**invalid_email_user_data)
