from pathlib import Path

from pytest import fixture


@fixture
def project_root_path() -> str:
    """Fixture providing the absolute path of the project's root directory.

    Returns:
        str: The absolute path of the project's root directory.
    """
    return str(Path(__file__).parent.parent.parent.parent)
