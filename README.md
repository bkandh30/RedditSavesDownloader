# 📥 RedditSavesDownloader

A Python script that automates the process of exporting your saved Reddit posts into a structured `.csv` file for offline reference and archival purposes.

## 🧾 Overview

Using the [PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/), this tool authenticates with your Reddit account and retrieves your saved posts, formatting them into a clean CSV file.

## 📦 Dependencies

- Python 3.x
- `praw`
- `python-dotenv`
- `typing`
- `os`
- `logging`
- `warnings`
- `csv`

Install dependencies using:

```bash
pip install module_name
```

## ⚙️ Setup Instructions

1. **Fork and Clone** the repository:

   ```bash
   git clone https://github.com/bkandh30/RedditSavesDownloader.git
   cd RedditSavesDownloader
   ```

2. **Configure Environment Variables**:
   - Create a `.env` file in the project root.
   - Copy the contents of `.env.example` into `.env`.
   - Fill in your Reddit app credentials:
     - `CLIENT_ID`
     - `CLIENT_SECRET`
     - `USERNAME`
     - `PASSWORD`

3. **Prepare Output File**:
   - Ensure a CSV file named `savedPosts.csv` exists.
   - Refer to `savedPostsSample.csv` for the correct format.

4. **Run the Script**:

   ```bash
   python3 main.py
   ```

## 🛠️ Usage Notes

- The script logs your saved posts and writes them in CSV format.
- Ensure your Reddit account has [API credentials](https://www.reddit.com/prefs/apps) created under the "script" type.
- Ideal for backup, offline reading, or personal data analysis.

## 🧾 License

This project is licensed under the [MIT License](LICENSE).
