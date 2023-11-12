from typing import Dict

from pytest import fixture


@fixture
def valid_config_data() -> Dict[str, str]:
    """Fixture for providing valid configuration data."""
    return {
        "DB_HOST": "localhost",
        "DB_PORT": "5432",
        "DB_NAME": "test_db",
        "DB_USER": "test_user",
        "DB_PASSWORD": "test_password",
    }
