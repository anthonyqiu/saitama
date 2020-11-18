import discord;
from discord.ext import commands;
import json;

#MEMBER LEAVE

#CONFIG
with open(r"Config.json", "r") as f:
    config = json.load(f);

class MemberLeave(commands.Cog):
    def __init__(self, client):
        self.client = client;

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        for channel in member.guild.channels:
            if channel.name == "general":
                emb = discord.Embed(title = "~M E M B E R   L E F T~", description = ":cry: " + member.mention + " has left the server", color = 0xffffff);
                emb.set_footer(text = config["defaultFooter"]);
                emb.set_author(name = config["name"], icon_url = config["profilePic"]);
                await channel.send(embed = emb);

def setup(client):
    client.add_cog(MemberLeave(client));