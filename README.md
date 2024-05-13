# RedditSavesDownloader

## Introduction
This is a script that I use to write my saved Reddit posts to a csv file.

## Dependencies
Python, Praw, Typing, OS, Python-Dotenv, Logging, Warnings, CSV

## Application Setup
To run the repository, follow these steps:
1. Star and Fork this repo to create your own copy to work from.
2. Clone the repository you forked to your local machine using:

   ```bash
      git clone <your_forked_repo_url>
   ```

3. Navigate to the root directory using command "cd server" and create a .env file and copy contents of .env.example file to .env file.

4. Create a savedPosts.csv file similar to savedPostsSample.csv file

5. Run:
   ```bash
     python3 main.py
   ```

## Usage
To use the app, update the following fields of the .env file:
- CLIENT_ID
- CLIENT_SECRET
- USERNAME
- PASSWORD
