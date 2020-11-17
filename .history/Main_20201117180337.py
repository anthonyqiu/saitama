import discord;
from discord.ext import commands;
import json;
import asyncio;
from itertools import cycle;

#CONFIG
with open(r"C:\Users\antho\Desktop\Saitama\Config.json", "r") as f:
    config = json.load(f);
client = commands.Bot(command_prefix = config["prefix"]);
client.remove_command("help");

async def change_status():
    await client.wait_until_ready();
    currentStatus = cycle(config["status"]);

    while not client.is_closed:
        current_status = next(currentStatus);
        await client.change_presence(game = discord.Game(name = current_status));
        await asyncio.sleep(120);

#EXTENSIONS / COGS
extensions = [
    "Economy",
    "Startup",
    "HelpCommand",
    "UtilCommands",
    "MiscCommands",
    "MusicCommands",
    "OnMessage",
    "Reaction",
    "MemberJoin",
    "MemberLeave",
    "LevelSystem"
];

@client.command()
async def load(extension):
    try:
        client.load_extension(extension);
        print("loaded {}".format(extension));
    except Exception as error:
        print("{} cannot be loaded. [{}]".format(extension, error));

@client.command()
async def unload(extension):
    try:
        client.unload_extension(extension);
        print("unloaded {}".format(extension));
    except Exception as error:
        print("{} cannot be unloaded. [{}]".format(extension, error));

if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension);
        except Exception as error:
            print("{} cannot be loaded. [{}]".format(extension, error));

#SETUP
client.loop.create_task(change_status());
client.run('''config["TOKEN"]''');