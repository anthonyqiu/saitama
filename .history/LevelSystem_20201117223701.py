import discord;
from discord.ext import commands;
import json;

#LEVELING SYSTEM

#CONFIG
with open(r"Config.json", "r") as f:
    config = json.load(f);

class LevelSystem(commands.Cog):
    def __init__(self, client):
        self.client = client;

    @commands.command(pass_context = True)
    async def level(self, ctx, user: discord.Member):
        with open(config["userDatabasePath"], "r") as f:
            users = json.load(f);
        emb = discord.Embed(title = "~{}'s   L E V E L~".format(user.name), description = "__");
        emb.set_author(name = config["name"], icon_url = config["profilePic"]);
        emb.set_footer(text = config["defaultFooter"]);
        emb.set_thumbnail(url = user.avatar_url);
        emb.add_field(name = "Level", value = "LVL " + str(users[f"{user.id}"]["level"]));
        emb.add_field(name = "Experience", value = str(users[f"{user.id}"]["experience"]) + " XP");
        await ctx.send(embed = emb);
        
    @commands.command(pass_context = True)
    async def level(self, ctx):
        user = ctx.author;
        with open(config["userDatabasePath"], "r") as f:
            users = json.load(f);
        emb = discord.Embed(title = "~{}'s   L E V E L~".format(user.name), description = "__");
        emb.set_author(name = config["name"], icon_url = config["profilePic"]);
        emb.set_footer(text = config["defaultFooter"]);
        emb.set_thumbnail(url = user.avatar_url);
        emb.add_field(name = "Level", value = "LVL " + str(users[f"{user.id}"]["level"]));
        emb.add_field(name = "Experience", value = str(users[f"{user.id}"]["experience"]) + " XP");
        await ctx.send(embed = emb);

def setup(client):
    client.add_cog(LevelSystem(client));