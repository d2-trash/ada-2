import asyncio

import discord
import event_handlers

HANDLERS = {
    "." + key: value
    for key, value in event_handlers.__dict__.items()
    if not key.startswith("__")
}


class Client(discord.Client):
    async def on_ready(self):
        print("Logged in as %s with id: %s" % (self.user.name, self.user.id))
        await self.change_presence(
            status=discord.Status.online, activity=discord.Game("with fire.")
        )

    async def on_message(self, message):
        r = HANDLERS.get(message.content.split(" ")[0].lower())
        if r is not None:
            await r(self, message)
        elif message.content.lower().startswith("good bot"):
            await message.channel.send("Good guardian.")


if __name__ == "__main__":
    with open("discord.secret", "r") as f:
        secret = f.read().rstrip("\n")
    client = Client()
    client.run(secret)
