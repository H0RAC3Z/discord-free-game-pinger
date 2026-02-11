# Discord Game Notification Bot

A simple Discord bot that tags a role when specific users post messages.

## Obtaining your Bot Token

1. Navigate to https://docs.discord.com/developers/intro and get to the developer portal

2. Create a new app

3. Enable Presence, Server Members, and Message Content Intents (you can tweak this as needed afterwards to run the bot minimally)

4. Refresh token and copy it to place in the .env file

## Setup

1. Clone the repo:
   git clone https://github.com/yourusername/discord-game-bot.git

2. Create Venv and Install dependencies:

   Create venv
   `python -m venv venv`

   Activate venv
   `source venv/bin/activate   # Mac/Linux`
   or
   `venv\Scripts\activate      # Windows`

   Install dependencies
   `pip install -r requirements.txt`

3. Create a `.env` file:

   DISCORD_BOT_TOKEN=your_bot_token_here
   STEAM_USER_ID=steam_discord_bot_id
   EPIC_USER_ID=steam_discord_bot_id
   PING_ROLE_ID=your_role_id

4. Run the bot:
   python main.py
