import json
import os
import csv


def save_json(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def save_csv(repositories: list[dict], filename: str):
    fields = ["name", "language", "stargazers_count", "forks_count"]

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields, extrasaction="ignore")

        writer.writeheader()
        writer.writerows(repositories)
