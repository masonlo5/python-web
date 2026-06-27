#######################模組#######################
import asyncio
import discord
import os
import requests
from dotenv import load_dotenv  # pip install python-dotenv
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


def build_forecast_embeds(forecast_summary):
    """根據天氣預報摘要資訊建立一個 Discord Embed 物件"""
    embeds = []

    for forecast in forecast_summary:
        embed = discord.Embed(
            title=f"{forecast['city_name']} 的天氣預報 - {forecast['datetime']}",
            description=f"describe :{forecast['description']}",
            color=discord.Color.from_str("0x1E90FF"),
        )

        icon_url = weather_api.get_icon_url(forecast["icon_code"])
        embed.set_thumbnail(url=icon_url)
        embed.add_field(
            name="Temperature",
            value=f"{forecast['temperature_celslus']} °C",
            inline=False,
        )
        embeds.append(embed)

    return embeds


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
async def weather(interaction: discord.Interaction, city: str, forecast: bool = False):
    """輸入 /weather <city_name> 就可以查詢該城市的天氣"""

    await interaction.response.defer()  # 告訴 Discord Bot 已經收到指令，正在處理中

    city = city.strip()  # 去除前後空白

    if not weather_api.api_key:
        await interaction.followup.send("API 金鑰未設定，請聯繫管理員。")
        return

    try:
        if not forecast:
            weather_summary = weather_api.get_weather_summary(city)
            if weather_summary is None:
                await interaction.followup.send(
                    f"找不到 {city} 的天氣資訊，請確認城市名稱是否正確。"
                )
                return

            embed = build_weather_embed(weather_summary)
            await interaction.followup.send(embed=embed)
            return

        forecast_summary = weather_api.get_forecast_summary(city)

    except (requests.RequestException, ValueError):
        await interaction.followup.send("無法取得天氣資訊，請稍後再試。")
        return

    if forecast_summary is None:
        await interaction.followup.send(
            f"找不到**{city}* 的天氣預報資訊，請確認城市名稱是否正確。"
        )
        return

    embeds = build_forecast_embeds(forecast_summary)
    await interaction.followup.send(embeds=embeds[:10])


#######################啟動#######################
def main():
    bot.run(os.getenv("DC_BOT_TOKEN"))


if __name__ == "__main__":
    main()
