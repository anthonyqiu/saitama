import discord;
from discord.ext import commands;
import json;

#UTILITY COMMANDS

#CONFIG
with open(r"Config.json", "r") as f:
    config = json.load(f);

class OnMessage(commands.Cog):
    def __init__(self, client):
        self.client = client;

    @commands.Cog.listener()
    async def on_message(self, message):
        with open(config["userDatabasePath"], "r") as f:
            userDatabase = json.load(f);

        await updateData(userDatabase, message.author);
        await updateExperience(userDatabase, message.author, 7);
        await updateBalance(userDatabase, message.author, 1)
        await levelUp(userDatabase, message.author, message.channel);

        with open(config["userDatabasePath"], "w") as f:
            json.dump(userDatabase, f, indent = 2);

async def updateData(userDatabase, author):
    if not f"{author.id}" in userDatabase:
        userDatabase[f"{author.id}"] = {};
        userDatabase[f"{author.id}"]["experience"] = 0;
        userDatabase[f"{author.id}"]["level"] = 0;
        userDatabase[f"{author.id}"]["balance"] = 0;
        userDatabase[f"{author.id}"]["permissions"] = [];

#LEVEL SYSTEM
async def updateExperience(userDatabase, author, exp):
    userDatabase[f"{author.id}"]["experience"] += exp;

async def levelUp(userDatabase, author, channel):
    experience = userDatabase[f"{author.id}"]["experience"];
    lvlStart = userDatabase[f"{author.id}"]["level"];
    lvlEnd = int(experience ** (1 / 4));

    if lvlStart < lvlEnd:
        coinsGained = userDatabase[f"{author.id}"]["level"] * 10;
        await updateBalance(userDatabase, author, coinsGained);
        emb = discord.Embed(title = "~L E V E L   U P !~", description = "{} is now level {}".format(author.mention, lvlEnd, color = 0xffffff));
        emb.set_thumbnail(url = author.avatar_url);
        emb.set_footer(text = config["defaultFooter"]);
        emb.set_author(name = config["name"], icon_url = config["profilePic"]);
        emb.add_field(name = "U   E A R N E D", value = "{} coins".format(coinsGained));
        await channel.send(embed = emb);
        userDatabase[f"{author.id}"]["level"] = lvlEnd;

#ECONOMY
async def updateBalance(userDatabase, author, amount):
    userDatabase[f"{author.id}"]["balance"] += amount;

def setup(client):
    client.add_cog(OnMessage(client));