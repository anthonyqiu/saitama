import discord;
from discord.ext import commands;
import json;

#MISC COMMANDS

#CONFIG
with open(r"Config.json", "r") as f:
    config = json.load(f);

class MiscCommands(commands.Cog):
    def __init__(self, client):
        self.client = client;

    @commands.command(pass_context = True)
    async def say(self, ctx, *, st):
        await ctx.send(st);

    @commands.command(pass_context = True)
    async def cookie(self, ctx):
        await ctx.send(":cookie:");

    #@commands.command(pass_context = True)
    #async def 

    @commands.command(pass_context = True)
    async def ping(self, ctx):
        await ctx.send(":ping_pong: Pong!");

    @commands.command(pass_context = True)
    async def pong(self, ctx):
        await ctx.send(":ping_pong: Ping!");

    @commands.command(pass_context = True)
    async def nepas(self, ctx):
        emb = discord.Embed(title = "~N E   P A S~", description = "It is starving and stupid it wraps around the first verb or the first part of the verb", color = 0xffffff);
        emb.set_footer(text = config["defaultFooter"]);
        emb.set_author(name = config["name"], icon_url = config["profilePic"]);
        await ctx.send(embed = emb);

    @commands.command(pass_context = True)
    async def butterdog(self, ctx):
        emb = discord.Embed(title = "~B U T T E R   D O G~", description = "The dog with the butter", color = 0xffffff);
        emb.set_image(url = "https://itk-assets.nyc3.cdn.digitaloceanspaces.com/2020/11/Screen-Shot-2020-11-10-at-1.33.43-PM-1620x911.jpg");
        emb.set_footer(text = config["defaultFooter"]);
        emb.set_author(name = config["name"], icon_url = config["profilePic"]);
        await ctx.send(embed = emb);

    @commands.command(pass_context = True)
    async def noU(self, ctx):
        await ctx.send("No U :no_entry_sign: :point_left:");

    @commands.command(pass_context = True)
    async def fbi(self, ctx):
        await ctx.send(":mega: FBI OPEN UP!!!");

    @commands.command(pass_context = True)
    async def onepunch(self, ctx):
        await ctx.send(":punch:");

    @commands.command(pass_context = True)
    async def saitama(self, ctx):
        emb = discord.Embed(title = "~S A I T A M A   I N   R E A L   L I F E~", description = "https://www.youtube.com/watch?v=7BnOPZMzrd8");
        emb.set_footer(text = config["defaultFooter"]);
        emb.set_author(name = config["name"], icon_url = config["profilePic"]);
        await ctx.send(embed = emb);

    @commands.command(pass_context = True)
    async def opmc(self, ctx):
        emb = discord.Embed(title = "~O N E   P U N C H   M A N   C H A L L E N G E~", description = "no days off", color = 0xffffff);
        emb.set_footer(text = config["defaultFooter"]);
        emb.set_author(name = config["name"], icon_url= config["profilePic"]);
        emb.add_field(name = "Push Ups", value = "100", inline=False);
        emb.add_field(name = "Sit Ups", value = "100", inline=False);
        emb.add_field(name = "Squats", value = "100", inline=False);
        emb.add_field(name = "Run", value = "10km", inline=False);
        emb.set_image(url = "https://i.stack.imgur.com/yCJUD.png");
        await ctx.send(embed = emb);

    @commands.command(pass_context = True)
    async def creator(self, ctx):
        emb = discord.Embed(title = "~C R E A T O R~", description = "Anthony Qiu", color = 0xffffff);
        await ctx.send(embed = emb);



def setup(client):
    client.add_cog(MiscCommands(client));