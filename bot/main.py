import os

import discord
from dotenv import load_dotenv

from bot.sentiment import sentiment_score


class Bot(discord.Client):
    scoreboard = {}

    async def on_ready(self):
        await self.change_presence(activity=discord.Game("Ready!"))

    async def on_message(self, message):

        bot = self.user
        name = message.author.name

        if message.author == bot:
            return

        if not self.scoreboard.get(name):
            self.scoreboard[name] = 0

        if message.content.startswith("/"):
            if "/clear" in message.content:
                await message.channel.purge(limit=999)
            if "/reset" in message.content:
                self.scoreboard = {}
            elif message.content == "/scoreboard":
                await message.channel.send(self.scoreboard)
            return

        previous_score = self.scoreboard[name]
        current_score = sentiment_score(message.content) * 100
        running_score = (previous_score + current_score) / 2
        self.scoreboard[name] = running_score


if __name__ == '__main__':
    load_dotenv()
    client = Bot(intents=discord.Intents.all())
    client.run(os.getenv("TOKEN"))
