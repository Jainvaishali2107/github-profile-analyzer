from reporadar.services.github_client import fetch_user_profile, fetch_user_repositories


class MockResponse:
    def __init__(self, status_code, data):
        self.status_code = status_code
        self.data = data

    def json(self):
        return self.data


def test_fetch_user_profile(monkeypatch):
    expected_data = {"login": "testuser"}

    def mock_get(*args, **kwargs):
        return MockResponse(200, expected_data)

    monkeypatch.setattr("reporadar.services.github_client.requests.get", mock_get)

    result = fetch_user_profile("testuser")

    assert result == expected_data


def test_fetch_user_repositories(monkeypatch):
    expected_data = [{"name": "Project-A"}]

    def mock_get(*args, **kwargs):
        return MockResponse(200, expected_data)

    monkeypatch.setattr("reporadar.services.github_client.requests.get", mock_get)

    result = fetch_user_repositories("testuser")

    assert result == expected_data
