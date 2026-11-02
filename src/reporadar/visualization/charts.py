import os
import matplotlib.pyplot as plt


def create_language_chart(language_count: dict, filename: str):
    if not language_count:
        print("No language data available for chart.")
        return

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    languages = list(language_count.keys())
    counts = list(language_count.values())

    plt.figure(figsize=(8, 8))

    plt.pie(counts, labels=languages, autopct="%1.1f%%", startangle=90)

    plt.title("GitHub Repository Language Distribution")
    plt.savefig(filename, bbox_inches="tight")
    plt.close()

    print(f"\nLanguage chart saved at: {filename}")
