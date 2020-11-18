import discord;
from discord.ext import commands;
import json;

#UTILITY COMMANDS

#CONFIG
with open(r"Config.json", "r") as f:
    config = json.load(f);

class UtilCommands(commands.Cog):
    def __init__(self, client):
        self.client = client;

    @commands.command(pass_context = True)
    async def info(self, ctx, author: discord.Member):
        with open(config["userDatabasePath"], "r") as f:
            users = json.load(f);
        emb = discord.Embed(title = "~{}'s   I N F O~".format(author.name), description = "Here's what I could find.",color = 0xffffff);
        emb.set_author(name = config["name"], icon_url = config["profilePic"]);
        emb.set_footer(text = config["defaultFooter"]);
        emb.add_field(name = "Name", value = author.name, inline = False);
        emb.add_field(name = "ID", value = author.id, inline = False);
        emb.add_field(name = "Status", value = author.status, inline = False);
        emb.add_field(name = "Highest Role", value = author.top_role, inline = False);
        emb.add_field(name = "Joined", value = author.joined_at, inline = False);
        emb.add_field(name = "Level", value = "LVL " + str(users[f"{author.id}"]["level"]));
        emb.add_field(name = "Balance", value = str(users[f"{author.id}"]["balance"]) + "coins");
        emb.set_thumbnail(url = author.avatar_url);
        await ctx.send(embed = emb);

    @commands.command(pass_context = True)
    async def clear(self, ctx, amount = 99):
        if amount <= 99:
            channel = ctx.message.channel;
            messages = [];
            async for message in channel.history(limit = int(amount) + 1):
                messages.append(message);
            await channel.delete_messages(messages);
            emb = discord.Embed(title = "~M E S S A G E S   D E L E T E D~", description = str(amount) + " messages removed", color = 0xffffff);
            emb.set_author(name = config["name"], icon_url = config["profilePic"]);
            emb.set_footer(text = config["defaultFooter"]);
            await ctx.send(embed = emb);
        else:
            emb = discord.Embed(title = "~E R R O R~", description = "exceeded maximum number of messages to be deleted", color = 0xffffff);
            emb.set_author(name = config["name"], icon_url = config["profilePic"]);
            emb.set_footer(text = config["defaultFooter"]);
            await ctx.send(embed = emb);

def setup(client):
    client.add_cog(UtilCommands(client));