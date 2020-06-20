import discord;
from discord.ext import commands;
import json;

#UTILITY COMMANDS

#CONFIG
with open(r"C:\Users\antho\Desktop\Saitama\Config.json", "r") as f:
    config = json.load(f);

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client;

    @commands.command(pass_context = True)
    async def balance(self, ctx, user: discord.Member):
        with open(config["userDatabasePath"], "r") as f:
            users = json.load(f);
        emb = discord.Embed(title = "~{}'s   B A L A N C E~".format(user.name), description = "__");
        emb.set_author(name = config["name"], icon_url = config["profilePic"]);
        emb.set_footer(text = config["defaultFooter"]);
        emb.set_thumbnail(url = user.avatar_url);
        emb.add_field(name = "Balance", value = str(users[f"{user.id}"]["balance"]) + " coins");
        await ctx.send(embed = emb);

    @commands.command(pass_context = True)
    async def selfBalance(self, ctx):
        user = ctx.author;
        with open(config["userDatabasePath"], "r") as f:
            users = json.load(f);
        emb = discord.Embed(title = "~{}'s   B A L A N C E~".format(user.name), description = "__");
        emb.set_author(name = config["name"], icon_url = config["profilePic"]);
        emb.set_footer(text = config["defaultFooter"]);
        emb.set_thumbnail(url = user.avatar_url);
        emb.add_field(name = "Balance", value = str(users[f"{user.id}"]["balance"]) + " coins");
        await ctx.send(embed = emb);
        
def setup(client):
    client.add_cog(Economy(client));