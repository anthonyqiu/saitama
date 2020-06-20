import discord;
from discord.ext import commands;
import json;

#REACTIONS

#CONFIG
with open(r"C:\Users\antho\Desktop\Saitama\Config.json", "r") as f:
    config = json.load(f);

class Reaction(commands.Cog):
    def __init__(self, client):
        self.client = client;

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel;
        emb = discord.Embed(title = "~R E A C T I O N !~", description = "{} has added {} to the message: {}".format(user.mention, reaction.emoji, reaction.message.content));
        emb.set_footer(text = config["defaultFooter"]);
        emb.set_author(name = config["name"], icon_url = config["profilePic"]);
        await channel.send( embed = emb);

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        channel = reaction.message.channel;
        emb = discord.Embed(title="~R E A C T I O N   R E M O V E D !~", description="{} has removed {} from the message: {}".format(user.mention, reaction.emoji, reaction.message.content));
        emb.set_footer(text = config["defaultFooter"]);
        emb.set_author(name = config["name"], icon_url = config["profilePic"]);
        await channel.send( embed = emb);

def setup(client):
    client.add_cog(Reaction(client));