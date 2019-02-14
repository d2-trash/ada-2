async def ping(client, message):
    await message.channel.send("Pong!")


async def register(client, message):
    await message.channel.send(
        f"Register at https://ada-2.cc/register?u={message.author.id}"
    )
