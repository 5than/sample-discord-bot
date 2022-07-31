
#Importing Required Modules, please use pip install discord , pip install json , pip intsall random , pip install time
import discord, json, random
from discord.ext import commands
from time import sleep

#loading variables
f = open('var.json', "r")
var = json.load(f)

botStatus = var["botStatus"]
botToken = var["botToken"]
botPrefix = var["botPrefix"]
onreadyMessageCheck = var["onreadyMessageCheck"]
onreadyMessage = var["onreadyMessage"]
errorMessageCheck = var["errorMessageCheck"]
errorMessage = var["errorMessage"]
commandOnePrompt = var["commandOnePrompt"]
commandOneResponse = var["commandOneResponse"]
commandTwoPrompt = var["commandTwoPrompt"]
commandTwoResponse = var["commandTwoResponse"]
commandThreePrompt = var["commandThreePrompt"]
commandThreeResponse = var["commandThreeResponse"]

botActivity = discord.Activity(name=botStatus, type=discord.ActivityType.listening)
bot = commands.Bot(command_prefix=botPrefix, activity=botActivity)
bot.remove_command('help')
intents = discord.Intents.default()
intents.members = True

if onreadyMessageCheck == "True":
    @bot.event
    async def on_ready():
        print(onreadyMessage)


@bot.command(name=commandOnePrompt)
async def one(ctx):
    await ctx.send(commandOneResponse)

@bot.command(name=commandTwoPrompt)
async def two(ctx):
    await ctx.send(commandTwoResponse)

@bot.command(name=commandThreePrompt)
async def three(ctx):
    await ctx.send(commandThreeResponse)


bot.run(botToken)
