#######################模組#######################
import asyncio
import discord
import os
from dotenv import load_dotenv #pip install python-dotenv
#######################初始化#######################
load_dotenv()

asyncio.set_event_loop(asyncio.new_event_loop())

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)
#######################事件#######################
@bot.event
async def on_ready():
    print(f"{bot.user} 已登入")
    await tree.sync()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == "hello":
        await message.channel.send("Hey!")


#######################指令#######################
@tree.command(name="hello", description="say hello to the bot")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hey!")
#######################啟動#######################
def main():
    bot.run(os.getenv("DC_BOT_TOKEN"))

if __name__ == "__main__":
    main()