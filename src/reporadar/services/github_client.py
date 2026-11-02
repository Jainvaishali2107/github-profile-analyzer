import requests
from reporadar.config import GITHUB_API_BASE_URL, REQUEST_TIMEOUT


def fetch_user_profile(username: str):
    url = f"{GITHUB_API_BASE_URL}/users/{username}"
    print(url)

    response = requests.get(url, timeout=REQUEST_TIMEOUT)
    data = response.json()

    if response.status_code == 404:
        if response.status_code == 404:
            print("User not found")
            return None

    elif response.status_code == 200:
        return data

    else:
        print("Something went wrong:", response.status_code)


def fetch_user_repositories(username: str):
    url = f"{GITHUB_API_BASE_URL}/users/{username}/repos"

    response = requests.get(url, timeout=REQUEST_TIMEOUT)

    if response.status_code == 200:
        repositories = response.json()
        return repositories

    elif response.status_code == 404:
        print("User not found")
        return None

    else:
        print("Something went wrong:", response.status_code)
        return None
