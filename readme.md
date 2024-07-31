
# Telegram CV Bot

This is a simple Telegram bot that showcases a personal resume/CV. It uses Python and the `python-telegram-bot` library. This bot includes commands to provide details about the user's contact information, experience, education, skills, and projects.


## Setup

1. Clone the repository:
    ```bash
    git clone 
    https://github.com/Sumitsonawane30/CV_Telegram_Bot
    cd telegram-cv-bot
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install python-telegram-bot
    ```

4. Create a new bot on Telegram and get the bot token. Replace the placeholder `BOT_TOKEN` in the code with your actual bot token.

5. Run the bot:
    ```bash
    python main.py
    ```

## Working Commands

Start a chat with your bot on Telegram and use the following commands to interact with it:

- `/start`: Welcomes the user.
- `/hello`: Greets the user by their first name.
- `/contact`: Provides the user's contact information..
- `/experience`: Lists the user's work experience.
- `/education`: Details the user's educational background.
- `/skills`: Lists the user's technical skills.
- `/projects`: Lists the user Projects.
