import discord;
from discord.ext import commands;
import json;
import lavalink;
from discord.utils import get;

#MUSIC COMMANDS

#CONFIG
with open(r"Config.json", "r") as f:
    config = json.load(f);

class MusicCommands(commands.Cog):
    def __init__(self, client):
        self.client = client;
        self.client.music = lavalink.Client(self.client.user.id);
        self.client.music.add_node("localhost", 7000, "q1w2E#R$", "na", "music-node");
        self.client.add_listener(self.client.music.voice_update_handler, 'on_socket_response')
        self.client.music.add_event_hook(self.track_hook)

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
    
    @commands.command(pass_context = True)
    async def play(self, ctx, url):
        

    @commands.command(pass_context = True)
    async def stop(self, ctx, url):
    
    async def track_hook(self, event):
        if isinstance(event, lavalink.events.QueueEndEvent):
            guild_id = int(event.player.guild_id)
            await self.connect_to(guild_id, None)

    async def connect_to(self, guild_id: int, channel_id: str):
        ws = self.bot._connection._get_websocket(guild_id)
        await ws.voice_state(str(guild_id), channel_id)

def setup(client):
    client.add_cog(MusicCommands(client));