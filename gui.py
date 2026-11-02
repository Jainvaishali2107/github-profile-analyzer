import tkinter as tk
from tkinter import ttk, messagebox

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from reporadar.services.github_client import fetch_user_profile, fetch_user_repositories
from reporadar.analysis.analyzer import analyze_languages
from reporadar.storage.file_manager import save_json, save_csv
from reporadar.visualization.charts import create_language_chart
from reporadar.reports.report_generator import generate_report


chart_canvas = None


def analyze():
    global chart_canvas

    username = username_entry.get().strip()

    if not username:
        messagebox.showwarning("Input Required", "Please enter a GitHub username.")
        return

    analyze_button.config(state="disabled", text="Analyzing...")
    status_label.config(text="Fetching GitHub data...")

    result_text.delete("1.0", tk.END)

    if chart_canvas is not None:
        chart_canvas.get_tk_widget().destroy()
        chart_canvas = None

    root.update_idletasks()

    try:
        # Fetch profile
        profile = fetch_user_profile(username)

        if not profile:
            messagebox.showerror("Error", "GitHub user not found.")
            return

        # Fetch repositories
        repositories = fetch_user_repositories(username)

        if repositories is None:
            messagebox.showerror("Error", "Unable to fetch repositories.")
            return

        # Save data
        save_json(profile, "data/raw/profile.json")
        save_json(repositories, "data/raw/repositories.json")
        save_csv(repositories, "data/processed/repositories.csv")

        # Analyze languages
        language_count = analyze_languages(repositories)

        # Generate chart image and report files
        create_language_chart(
            language_count, "data/processed/language_distribution.png"
        )

        generate_report(profile, repositories, language_count)

        # Display profile
        result_text.insert(tk.END, "========== GITHUB PROFILE ==========\n\n")

        result_text.insert(tk.END, f"Name: {profile.get('name') or 'Not provided'}\n")
        result_text.insert(tk.END, f"Username: {profile.get('login')}\n")
        result_text.insert(tk.END, f"Bio: {profile.get('bio') or 'No bio available'}\n")
        result_text.insert(
            tk.END, f"Public Repositories: {profile.get('public_repos', 0)}\n"
        )
        result_text.insert(tk.END, f"Followers: {profile.get('followers', 0)}\n")
        result_text.insert(tk.END, f"Following: {profile.get('following', 0)}\n")
        result_text.insert(
            tk.END, f"Location: {profile.get('location') or 'Not provided'}\n"
        )

        # Display repositories
        result_text.insert(tk.END, "\n========== REPOSITORIES ==========\n")

        for index, repo in enumerate(repositories, start=1):
            result_text.insert(
                tk.END,
                f"\n{index}. {repo.get('name')}\n"
                f"   Language: {repo.get('language') or 'Not specified'}\n"
                f"   Stars: {repo.get('stargazers_count', 0)}\n"
                f"   Forks: {repo.get('forks_count', 0)}\n",
            )

        # Display language analysis
        result_text.insert(tk.END, "\n========== LANGUAGE ANALYSIS ==========\n")

        total = sum(language_count.values())

        if total:
            for language, count in language_count.items():
                percentage = (count / total) * 100

                result_text.insert(
                    tk.END, f"{language}: {count} repositories ({percentage:.2f}%)\n"
                )
        else:
            result_text.insert(tk.END, "No language data available.\n")

        result_text.insert(
            tk.END, "\nCSV, JSON and Markdown report generated successfully!"
        )

        # Render pie chart directly inside Tkinter
        if language_count:
            fig = Figure(figsize=(6, 5), dpi=100)
            ax = fig.add_subplot(111)

            ax.pie(
                language_count.values(),
                labels=language_count.keys(),
                autopct="%1.1f%%",
                startangle=90,
            )

            ax.set_title("GitHub Language Distribution")

            fig.tight_layout()

            chart_canvas = FigureCanvasTkAgg(fig, master=chart_frame)

            chart_canvas.draw()

            chart_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, pady=10)

        status_label.config(text="Analysis completed successfully!")

    except Exception as error:
        messagebox.showerror("Error", str(error))
        status_label.config(text="Something went wrong.")

    finally:
        analyze_button.config(state="normal", text="Analyze")


# Main window
root = tk.Tk()
root.title("RepoRadar - GitHub Developer Intelligence")
root.geometry("900x850")
root.configure(bg="#f4f7f6")


# Heading
title = tk.Label(
    root, text="RepoRadar", font=("Arial", 26, "bold"), bg="#f4f7f6", fg="#176b50"
)
title.pack(pady=(20, 5))


subtitle = tk.Label(
    root, text="GitHub Developer Intelligence System", font=("Arial", 11), bg="#f4f7f6"
)
subtitle.pack(pady=5)


# Input section
input_frame = tk.Frame(root, bg="#f4f7f6")
input_frame.pack(pady=20)

tk.Label(input_frame, text="GitHub Username:", font=("Arial", 11), bg="#f4f7f6").pack(
    side=tk.LEFT, padx=5
)


username_entry = ttk.Entry(input_frame, width=30, font=("Arial", 11))
username_entry.pack(side=tk.LEFT, padx=5)


analyze_button = tk.Button(
    input_frame,
    text="Analyze",
    command=analyze,
    bg="#176b50",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=15,
    pady=5,
)
analyze_button.pack(side=tk.LEFT, padx=5)


# Scrollable area
content_frame = tk.Frame(root, bg="#f4f7f6")
content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

canvas = tk.Canvas(content_frame, bg="#f4f7f6", highlightthickness=0)

scrollbar = ttk.Scrollbar(content_frame, orient=tk.VERTICAL, command=canvas.yview)

scrollable_frame = tk.Frame(canvas, bg="#f4f7f6")

scrollable_frame.bind(
    "<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.bind(
    "<Configure>", lambda event: canvas.itemconfig(canvas_window, width=event.width)
)

canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


# Results
result_text = tk.Text(
    scrollable_frame,
    height=28,
    font=("Consolas", 10),
    wrap=tk.WORD,
    bg="white",
    fg="#222222",
)

result_text.pack(fill=tk.X, pady=10)


# Chart section
chart_heading = tk.Label(
    scrollable_frame,
    text="LANGUAGE DISTRIBUTION",
    font=("Arial", 16, "bold"),
    bg="#f4f7f6",
    fg="#176b50",
)

chart_heading.pack(pady=10)


chart_frame = tk.Frame(scrollable_frame, bg="#f4f7f6")

chart_frame.pack(fill=tk.BOTH, expand=True, pady=10)


# Status
status_label = tk.Label(
    root,
    text="Enter a GitHub username to begin.",
    font=("Arial", 10),
    bg="#f4f7f6",
    fg="#176b50",
)

status_label.pack(pady=10)


root.mainloop()
