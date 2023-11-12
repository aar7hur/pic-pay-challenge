from glob import glob


def refactor(string: str) -> str:
    """Method that adjusts (sub)module paths for importing.

    Args:
        string (str): (Sub)Module path

    Returns:
        str: Adjusted (sub)module path
    """
    return string.replace("/", ".").replace("\\", ".").replace(".py", "")


pytest_plugins = [refactor(fixture) for fixture in glob("picpaychallenge/tests/fixtures/[!_]*.py")]
