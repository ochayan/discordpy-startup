from discord.ext import commands
import os
import traceback
import random

if messae.content == "スロット":
    slot_list = ['\U00002660', '\U00002663', '\U00002665', '\U00002666', ':seven:']
    A = random.choice(slot_list)
    B = random.choice(slot_list)
    C = random.choice(slot_list)
    await client.send_message(message.channel, "%s%s%s" % (A, B, C))

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def シグ(ctx):
    await ctx.send('シグシグ')


bot.run(token)
