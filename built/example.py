import discord
bot = discord.Bot()
token = "yourtokenhere"



@bot.event
async def on_ready():

    print("eee")

    



@bot.event
async def on_member_join(ctx):

    await ctx.reply(f"welcome {ctx.author.mention()}")

    



@bot.slash_command()
async def ping(ctx):

    await ctx.reply(f"pong")

    



@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return

    if {ctx.content} == "sus":

        await ctx.reply(f"no u")

        

    


bot.run(token)