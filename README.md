# 🚀 RepoRadar — GitHub Developer Intelligence System

**RepoRadar** is a Python-based GitHub Developer Intelligence System designed to collect, organize, and analyze GitHub developer and repository data.

The goal of this project is to transform raw GitHub API data into meaningful developer insights through data collection, analysis, visualization, and report generation.

This project is being built as part of my journey into **Python Development and AI Engineering**, with a focus on clean code, modular architecture, API integration, and practical software development.

---

## 🎯 Project Objectives

- Fetch developer profile information using the GitHub REST API.
- Retrieve public repositories of a GitHub user.
- Analyze repository and developer activity.
- Generate meaningful insights from GitHub data.
- Store collected data for future analysis.
- Visualize developer statistics through charts.
- Generate structured developer reports.

## ✨ Features

### Implemented

- Accepts a GitHub username from the user.
- Constructs the GitHub API profile endpoint dynamically.
- Makes HTTP requests using the Requests library.
- Fetches GitHub user profile information.
- Handles HTTP response status codes.
- Handles invalid usernames and 404 responses.
- Uses a modular project structure.

### Planned Features

- Fetch public repositories.
- Analyze repository statistics and programming languages.
- Calculate developer activity insights.
- Store API responses in structured files.
- Generate charts and visualizations.
- Generate developer intelligence reports.
- Add improved error handling and logging.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.13+ | Core programming language |
| GitHub REST API | Developer and repository data |
| Requests |
| UV | Dependency and environment management |
| JSON | API response format and data storage |
| Matplotlib | Planned data visualization |
| Pytest | Planned testing |

## 📁 Project Structure

```text
RepoRadar/
│
├── main.py
├── pyproject.toml
├── uv.lock
├── .env
├── .gitignore
├── README.md
│
└── src/
    └── reporadar/
        │
        ├── config.py
        │
        ├── models/
        │   └── github_models.py
        │
        ├── services/
        │   └── github_client.py
        │
        ├── analysis/
        │   └── analyzer.py
        │
        ├── storage/
        │   └── file_manager.py
        │
        ├── visualization/
        │   └── charts.py
        │
        └── reports/
```

### Architecture Overview

- **main.py:** Application entry point and execution flow.
- **config.py:** Centralized configuration such as API base URL and request timeout.
- **models/:** Structured representations of GitHub data.
- **services/:** GitHub API communication and data retrieval.
- **analysis/:** Developer and repository data analysis.
- **storage/:** Data persistence and file management.
- **visualization/:** Charts and graphical representations.
- **reports/:** Developer intelligence report generation.

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Jainvaishali2107/RepoRadar.git
```

```bash
cd RepoRadar
```

### 2. Create a virtual environment

```bash
uv venv --python 3.13
```

### 3. Activate the environment

For Git Bash:

```bash
source .venv/Scripts/activate
```

### 4. Install dependencies

```bash
uv sync
```

If setting up dependencies for the first time:

```bash
uv add requests
```

## ▶️ Run the Project

```bash
uv run python main.py
```

Enter a GitHub username when prompted.

The application currently fetches the corresponding GitHub user profile using the GitHub REST API.

## 🔗 API Integration

RepoRadar currently uses the GitHub REST API.

**User Profile Endpoint:**

```text
https://api.github.com/users/jainvaishali2107
```

Example:

```text
https://api.github.com/users/octocat
```

The API provides information such as:

- Username
- Name
- Bio
- Location
- Public repository count
- Followers
- Following
- GitHub profile URL

## 📚 Concepts Practiced

This project provides practical experience with:

- Python functions and modules
- Object-oriented programming
- API integration and HTTP requests
- JSON data handling
- Exception handling
- Environment and dependency management
- Modular application architecture
- Data analysis and visualization (planned)

## 🗺️ Development Roadmap

- [x] Initial project setup
- [x] GitHub API integration
- [x] Fetch user profile information
- [x] Basic HTTP response handling
- [ ] Fetch public repositories
- [ ] Create structured GitHub data models
- [ ] Implement repository analysis
- [ ] Store collected data
- [ ] Generate visualizations
- [ ] Generate developer reports
- [ ] Add unit tests
- [ ] Improve application reliability

## 🌱 Learning Journey

RepoRadar is an evolving project. I'm building it step by step, focusing on understanding the concepts behind every feature rather than simply implementing code.

The long-term vision is to develop it into a complete developer intelligence application that turns GitHub activity into useful insights.

## 👩‍💻 Author

**Vaishali Jain**

Third-year B.Tech Computer Science Engineering Student

GitHub: [@Jainvaishali2107](https://github.com/Jainvaishali2107)

---

⭐ If you find this project interesting, feel free to explore the repository!