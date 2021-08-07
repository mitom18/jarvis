import random
import yaml
import discord
from discord.activity import Game
from service.joke import get_programming_joke
from discord.ext import commands
from os import path


def read_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


config = read_yaml(
    path.join(
        path.dirname(path.abspath(__file__)),
        "config.yml"
    )
)

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix=config["BOT_PREFIX"],
    intents=intents,
    owner_id=int(config["BOT_OWNER_ID"])
)


@bot.event
async def on_ready():
    await bot.change_presence(activity=Game(name='Real life'))
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')


@bot.command(description='Prints current ping.')
async def ping(ctx: commands.Context):
    await ctx.send(f'Pong in {round(bot.latency * 1000)} ms!')


@bot.command(description='Retrieves random programming joke.')
async def joke(ctx: commands.Context):
    joke = get_programming_joke()
    color = random.randint(0, 0xFFFFFF)
    embed = discord.Embed(
        title="Random joke", description=joke, color=color)
    await ctx.send(embed=embed)


def main():
    bot.run(config["DISCORD_BOT_TOKEN"])


if __name__ == '__main__':
    main()
