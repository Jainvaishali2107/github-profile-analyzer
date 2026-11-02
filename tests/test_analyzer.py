from reporadar.analysis.analyzer import analyze_languages


def test_analyze_languages(sample_repositories):
    result = analyze_languages(sample_repositories)

    assert result == {"Python": 2, "JavaScript": 1}


def test_empty_repositories():
    result = analyze_languages([])

    assert result == {}
