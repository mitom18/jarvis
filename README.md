# Jarvis Discord Bot

Discord bot written for my Discord server. It has no special functionality, commands are created according to my recent ideas and interests.

Built with Python 3.9.5 and [discord.py](https://github.com/Rapptz/discord.py) module.

## Usage

You can run the bot on background with shell scripts located in the `bin` directory. Just open your bash command line in the project root directory and use commands shown below.

```
# Start the bot as a background task.
./bin/start.sh

# Stop the running bot.
./bin/stop.sh

# Deploy the newest bot version from GitHub (requires SSH connection to this repo).
./bin/deploy.sh
```

Or you can just simply run the main `jarvis.py` file with Python 3.9 or higher.

```
python3 jarvis.py
```

## Licence
MIT
