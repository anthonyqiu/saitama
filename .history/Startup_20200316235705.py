import discord;
from discord.ext import commands;

class Startup(commands.Cog):
    def __init__(self, client):
        self.client = client;

        @client.event
        async def on_ready():
            print("W E L C O M E   A N T H O N Y");
            print("I am running on {}\n".format(client.user.name));

def setup(client):
    client.add_cog(Startup(client));