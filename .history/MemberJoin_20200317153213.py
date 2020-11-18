import discord;
from discord.ext import commands;
import json;

#MEMBER JOIN

#CONFIG
with open(r"C:\Users\antho\Desktop\Saitama\Config.json", "r") as f:
    config = json.load(f);

class MemberJoin(commands.Cog):
    def __init__(self, client):
        self.client = client;

    @commands.Cog.listener()
    async def on_member_join(self, member):
        for channel in member.guild.channels:
            if channel.name == "general":
                emb = discord.Embed(title = "~N E W   M E M B E R !~", description = ":ok_hand: " + member.mention + " has joined the server", color = 0xffffff);
                emb.set_footer(text = config["defaultFooter"]);
                emb.set_author(name = config["name"], icon_url = config["profilePic"]);
                await channel.send(embed = emb);

        #USESR DATABASE
        with open(repr(config["userDatabasePath"]), "r") as f:
            stats = json.load(f);

        await updateData(stats, member);

        with open(repr(config["userDatabasePath"]), "w") as f:
            json.dump(stats, f);

async def updateData(userDatabase, author):
    if not f"{author.id}" in userDatabase:
        userDatabase[f"{author.id}"] = {};
        userDatabase[f"{author.id}"]["experience"] = 0;
        userDatabase[f"{author.id}"]["level"] = 0;
        userDatabase[f"{author.id}"]["balance"] = 0;
        userDatabase[f"{author.id}"]["permissions"] = [];

def setup(client):
    client.add_cog(MemberJoin(client));