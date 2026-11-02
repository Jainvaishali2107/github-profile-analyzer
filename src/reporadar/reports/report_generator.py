import os


def generate_report(
    profile: dict,
    repositories: list[dict],
    language_count: dict,
    filename: str = "reports/report.md",
):

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    total_languages = sum(language_count.values())

    with open(filename, "w", encoding="utf-8") as file:
        file.write("# RepoRadar - Developer Report\n\n")

        file.write("## GitHub Profile\n\n")
        file.write(f"- **Name:** {profile.get('name') or 'Not provided'}\n")
        file.write(f"- **Username:** {profile.get('login')}\n")
        file.write(f"- **Bio:** {profile.get('bio') or 'No bio'}\n")
        file.write(f"- **Public Repositories:** {profile.get('public_repos', 0)}\n")
        file.write(f"- **Followers:** {profile.get('followers', 0)}\n")
        file.write(f"- **Following:** {profile.get('following', 0)}\n\n")

        file.write("## Repository Details\n\n")
        file.write("| Repository | Language | Stars | Forks |\n")
        file.write("|---|---|---:|---:|\n")

        for repo in repositories:
            file.write(
                f"| {repo.get('name')} "
                f"| {repo.get('language') or 'Not specified'} "
                f"| {repo.get('stargazers_count', 0)} "
                f"| {repo.get('forks_count', 0)} |\n"
            )

        file.write("\n## Language Analysis\n\n")

        for language, count in language_count.items():
            percentage = (count / total_languages) * 100
            file.write(f"- **{language}:** {count} repositories ({percentage:.2f}%)\n")

        file.write("\n## Summary\n\n")
        file.write(f"- Total repositories fetched: {len(repositories)}\n")
        file.write(f"- Different languages used: {len(language_count)}\n")

    print(f"\nReport generated at: {filename}")
