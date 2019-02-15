import jwt

with open("jwt.secret", "r") as f:
    JWT_SECRET = f.read().rstrip("\n")


async def ping(client, message):
    await message.channel.send("Pong!")


async def register(client, message):
    await message.channel.send(
        "I've sent registration instructions to you _privately_."
    )
    await message.author.send(
        f"Register at https://www.bungie.net/en/oauth/authorize?client_id=26007&response_type=code&state={ jwt.encode({'user': message.author.id}, JWT_SECRET, algorithm='HS256').decode('utf-8') }"
    )
