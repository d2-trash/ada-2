from bot import Client
from redis import Redis

with open("secrets/discord.secret", "r") as f:
    DISCORD_SECRET = f.read().rstrip("\n")

REDIS = Redis(host="db", port=6379, db=0)


DISCORD = Client()
DISCORD.run(DISCORD_SECRET)
