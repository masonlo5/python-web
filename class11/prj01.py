#######################模組#######################
import asyncio
import discord
import os
import requests
from dotenv import load_dotenv #pip install python-dotenv
from myfunction.myfunction import WeatherAPI
#######################初始化#######################
load_dotenv()

asyncio.set_event_loop(asyncio.new_event_loop())

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(bot)
weather_api = WeatherAPI(os.getenv("Weather_API_KEY"))

def build_weather_embed(weather_summary):
    """根據天氣摘要資訊建立一個 Discord Embed 物件"""
    embed = discord.Embed(
        title=f"{weather_summary['city_name']} 的天氣",
        description=f"describe :{weather_summary['description']}",
        color=discord.Color.from_str("0x1E90FF"),
    )

    icon_url = weather_api.get_icon_url(weather_summary["icon_code"])
    embed.set_thumbnail(url=icon_url)

    embed.add_field(
        name="Temperature",
        value=f"{weather_summary['temperature_celslus']} °C",
        inline=False,
    )
    return embed
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

@tree.command(name="weather", description="查詢指定城市的天氣")
async def weather(interaction: discord.Interaction, city_name: str):
    """輸入 /weather <city_name> 就可以查詢該城市的天氣"""

    await interaction.response.defer()  # 告訴 Discord Bot 已經收到指令，正在處理中

    city = city.strip()  # 去除前後空白

    if not weather_api.api_key:
        await interaction.followup.send("API 金鑰未設定，請聯繫管理員。")
        return
#######################啟動#######################
def main():
    bot.run(os.getenv("DC_BOT_TOKEN"))

if __name__ == "__main__":
    main()