import discord
from discord.ext import commands
import random
from ToxicCheck import evaluate
client = commands.Bot(command_prefix="")

@client.event
async def on_ready():
	print("bot is ready.")

@client.command()
async def ping(ctx):
	await ctx.send(f"> Pong! {round(client.latency * 1000)}ms")

@client.command(aliases=['isToxic', 'Istoxic', 'istoxic'])
async def toxx(ctx, *, sentence):
	preds = evaluate(sentence.lower())
	await ctx.send(f"The sentence was {(preds[0][0] * 100):2f} % Toxic")

@client.command()
async def stop(ctx):
	await ctx.send("stopping")
	exit()

#client.run(YOUR UNIQUE DISCORD CODE)