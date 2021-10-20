import os

global indents
pyLine = ""
writeContent = []
indents = 0

def parseArgs():
    args = []
    arg = ""
    isArg = False
    for i in range(len(line)-1):
        if line[i - 1] == "(":
            isArg = True
        if isArg == True and line[i] != ",":
            arg += line[i]
        if line[i + 1] == ",":
            args.append(arg)
            arg = ""
        if line[i+1] == ")":
            isArg = False
            args.append(arg)
    return args


for file in os.listdir("sus"):
    susfile = open(f"sus/{file}")

    for line in susfile.readlines():   # theres probably a better way to do this then a bunch of if statements
        line = line.strip(" ")
        if "command" in line.lower():
            args = parseArgs()
            line = f"@bot.slash_command()\nasync def {args[0]}(ctx):\n"
            indents += 1
        if "onmessagesent" in line.lower():
            line = f"@bot.event\nasync def on_message(ctx):\n    if ctx.author == bot.user:\n        return\n"
            indents += 1

        if "onready" in line.lower():
            line = f"@bot.event\nasync def on_ready():\n"
            indents += 1
        if "onmemberjoin" in line.lower():
            line = f"@bot.event\nasync def on_member_join(ctx):\n"
            indents += 1

        if line.lower().startswith("if"):
            indents += 1

        if "end" in line.lower():
            indents -= 1
            line = "\n"

        if "reply" in line.lower():
            args = parseArgs()
            line = f"await ctx.reply(f{args[0]})\n"



        line = line.replace("--authorMention", "{ctx.author.mention()}")
        line = line.replace("--messageContent", "{ctx.content}")

        line += "\n" + "    " * indents
        pyLine = line
        writeContent.append(pyLine)

    pyFile = file.removesuffix(".sus")
    if f"{pyFile}.py" not in os.listdir("built"):
        open(f"built/{pyFile}.py", "x")
    open(f"built/{pyFile}.py", "w").write("")
    py = open(f"built/{pyFile}.py", "a")

    py.write("import discord\nbot = discord.Bot()\n")
    py.writelines(writeContent)
    py.write("\nbot.run(token)")
