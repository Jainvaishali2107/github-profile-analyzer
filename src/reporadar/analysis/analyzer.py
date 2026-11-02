def analyze_languages(repositories: list[dict]):
    language_count = {}

    for repo in repositories:
        language = repo.get("language")

        if language is not None:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1

    print("\n========== LANGUAGE ANALYSIS ==========")

    for language, count in language_count.items():
        print(f"{language}: {count} repositories")

    total = sum(language_count.values())

    print("\n========== LANGUAGE DISTRIBUTION ==========")

    if total > 0:
        for language, count in language_count.items():
            percentage = (count / total) * 100
            print(f"{language}: {percentage:.2f}%")
    else:
        print("No programming language data available.")

    return language_count
