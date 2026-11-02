import time

from reporadar.services.github_client import fetch_user_profile, fetch_user_repositories
from reporadar.analysis.analyzer import analyze_languages
from reporadar.storage.file_manager import save_json, save_csv
from reporadar.visualization.charts import create_language_chart
from reporadar.reports.report_generator import generate_report


print("=" * 30)
print("      WELCOME TO REPORADAR")
print("=" * 30)

print("\nGITHUB DEVELOPER INTELLIGENCE SYSTEM")

print("\nApplication is starting...")
time.sleep(2)

print("Please wait...")

username = input("\nEnter GitHub username: ")

profile = fetch_user_profile(username)

if profile:
    print("\n" + "=" * 30)
    print("       GITHUB PROFILE")
    print("=" * 30)

    print("Name:", profile.get("name") or "Not provided")
    print("Username:", profile.get("login") or "Not available")
    print("Bio:", profile.get("bio") or "No bio available")
    print("Public Repositories:", profile.get("public_repos", 0))
    print("Followers:", profile.get("followers", 0))
    print("Following:", profile.get("following", 0))
    print("Location:", profile.get("location") or "Not provided")

    # Save profile data
    save_json(profile, "data/raw/profile.json")

    # Fetch repositories
    repositories = fetch_user_repositories(username)

    if repositories is not None:
        print("\nTotal repositories fetched:", len(repositories))
        print("\n========== REPOSITORIES ==========")

        # Save repository data
        save_json(repositories, "data/raw/repositories.json")
        save_csv(repositories, "data/processed/repositories.csv")

        # Display repositories
        for index, repo in enumerate(repositories, start=1):
            print(f"\nRepository {index}")
            print("Name:", repo.get("name"))
            print("Language:", repo.get("language") or "Not specified")
            print("Stars:", repo.get("stargazers_count", 0))
            print("Forks:", repo.get("forks_count", 0))
            print("-" * 35)

        # Analyze programming languages
        language_count = analyze_languages(repositories)

        # Generate language pie chart
        create_language_chart(
            language_count, "data/processed/language_distribution.png"
        )

        # Generate developer report
        generate_report(profile, repositories, language_count)

        print("\n" + "=" * 30)
        print("       REPORADAR COMPLETED")
        print("=" * 30)

    else:
        print("Unable to fetch repositories.")

else:
    print("Unable to fetch GitHub profile.")
