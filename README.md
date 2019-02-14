# Ada-2

Ada-2 is an Automatic Discord Administrator for managing our Destiny 2 clan Discord.

## Commands

All commands are prepended with a `.` (period).

- `.ping`
-

## Installation

Run the `install.sh` script.  _Built for python3.7, ymmv with other versions._

## Setup

- Register an application with [Discord](https://discordapp.com/developers/applications/).
  1. `Create an application` and give it a name (this is not your bots name)
  2. Navigate to `Bot` under the `Settings` toolbar on the left
     1. `Add Bot`
     2. Copy the bots token to `secrets/discord`
     3. Set the bot to private
  3. Go to the OAuth2
     1. Select the `bot` scope
     2. Under `Bot Permissions`, check `Send Messages`
     3. Go to the generate OAuth2 link and invite the bot to your server
- Register an application with [Bungie](https://www.bungie.net/en/Application).
    1. Copy the API key to `secrets/bungie`
    2. TODO

## TODO

- Register a `.bot` domain with Amazon
- PoC Bungie side of bot, and add to [setup](#setup)










https://github.com/tiangolo/meinheld-gunicorn-flask-docker