import discord;
from discord.ext import commands;
import json;

#HELP COMMAND

#CONFIG
with open(r"C:\Users\antho\Desktop\Saitama\Config.json", "r") as f:
    config = json.load(f);
with open(r"C:\Users\antho\Desktop\Saitama\Commands.json", "r") as f:
    commandsFile = json.load(f);

class HelpCommand(commands.Cog):
    def __init__(self, client):
        self.client = client;

    @commands.command(pass_context=True)
    async def help(self, ctx):
        author = ctx.message.author;
        emb = discord.Embed(title = "~H E L P~", description="__", color = 0xffffff);
        emb.set_footer(text = "End of .help");
        emb.set_author(name = config["name"], icon_url = config["profilePic"]);

        for command in commandsFile["commands"]:
            emb.add_field(name = config["prefix"] + command["name"], value = command["description"], inline = False);
        await ctx.send(author, embed = emb);

def setup(client):
    client.add_cog(HelpCommand(client));