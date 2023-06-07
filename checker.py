import requests


def check(nickname: str) -> bool:
    """
    Check if the nickname is available.

    :param nickname: nickname to check
    :return: True if the nickname is available, False otherwise
    """
    url = f"https://api.mojang.com/users/profiles/minecraft/{nickname}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return False
    except requests.exceptions.HTTPError:
        return True
