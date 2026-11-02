import pytest


@pytest.fixture
def sample_repositories():
    return [
        {
            "name": "Project-A",
            "language": "Python",
            "stargazers_count": 5,
            "forks_count": 2,
        },
        {
            "name": "Project-B",
            "language": "JavaScript",
            "stargazers_count": 3,
            "forks_count": 1,
        },
        {
            "name": "Project-C",
            "language": "Python",
            "stargazers_count": 1,
            "forks_count": 0,
        },
    ]


@pytest.fixture
def sample_profile():
    return {
        "name": "Vaishali",
        "login": "jainvaishali2107",
        "bio": "Developer",
        "public_repos": 3,
        "followers": 1,
        "following": 3,
    }
