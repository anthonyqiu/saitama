import discord;
from discord.ext import commands;
import json;
import youtube_dl;
from discord.utils import get;

#MUSIC COMMANDS

#CONFIG
with open(r"Config.json", "r") as f:
    config = json.load(f);

class MusicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client;

    @commands.command(pass_context = True)
    async def summon(self, ctx):
        channel = ctx.message.author.voice.channel;
        voice = get(self.client.voice_clients, guild = ctx.guild);

        if voice and voice.is_connected():
            await voice.move_to(channel);
        else:
            voice = await channel.connect();

        print("{} is currently connected to {}\n".format(config["name"], channel));

    @commands.command(pass_context = True)
    async def leave(self, ctx):
        channel = ctx.message.author.voice.channel;
        voice = get(self.client.voice_clients, guild = ctx.guild);

        if voice and voice.is_connected():
            await voice.disconnect();
            print("{} has left {}\n".format(config["name"], channel));
        else:
            voice = await channel.connect();
            print("{} is not in a voice channel".format(config["name"]));

def setup(client):
    client.add_cog(MusicCommands(client));