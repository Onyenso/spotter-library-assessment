import re


def validate_password(password: str) -> bool:
    """
    Checks if password meets the requirements and if so,
    returns a boolean. Does not sanitize password

    Passwords must be at least 6 characters and contain at least 1 from each
    of the following categories
        * Uppercase letters: A-Z.
        * Lowercase letters: a-z.
        * Numbers: 0-9.
        * Symbols: !@?&#$%

    Passwords cannot contain any whitespace characters, note that
    leading and trailing whitespace is automatically trimmed by
    the serializer.
    """

    if password is None:
        return False

    # Check if password meets length requirements
    if len(password) < 6:
        return False

    # check if password contains any form of whitespace
    whitespace_regex = r"\s"
    whitespace_match = re.search(whitespace_regex, password)

    # If whitespace is found return False
    if whitespace_match is not None:
        return False

    # Check if the password meets the character requirements using regex
    password_regex = (
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@?&#$%])[A-Za-z\d!@?&#$%]{6,}$"
    )

    password_match = re.fullmatch(password_regex, password)

    # If password was matched correctly the return bool
    return password_match is not None
