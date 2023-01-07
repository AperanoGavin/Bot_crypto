import discord
import io
import requests
import time
from discord import app_commands
from deep_translator import GoogleTranslator
from binance.client import Client
from dotenv import load_dotenv
load_dotenv()
import os
token = os.getenv("TOKEN")
binance = os.getenv("BINANCE_API_KEY")
binance_secret_key = os.getenv("BINANCE_SECRET_KEY")

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
GUILD = os.getenv('1047812022789734480')
#intents = discord.Intents.default()
#intents.message_content = True
@client.event
async def on_ready():
    synced = await tree.sync()
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

#andrew motivation 
@tree.command(name="andrew" , description="petit message de motivation")
async def foot( interaction: discord.Interaction):
    url = requests.get("https://www.tateapi.com/api/quote")
    url_quote = url.json()["quote"]
    get_quote_translate = GoogleTranslator(source='auto', target='fr').translate(url_quote)
    await interaction.response.send_message(get_quote_translate)        

#crypto (binance) bitcoin








# Seuils de prix définis dans votre stratégie
buy_threshold = 1000
sell_threshold = 1100

# Quantité de cryptomonnaie à acheter ou vendre
order_size = 0.1

# ID de produit de Binance (par exemple, BTCUSDT pour le Bitcoin en dollars américains)
product_id = 'BTCUSDT'

# récupère le prix du btc actuel
client_binance = Client(binance, binance_secret_key)
get_btc_price = client_binance.get_symbol_ticker(symbol=product_id)
price = get_btc_price["price"]
print(price)



@tree.command(name="btc" , description="prix du btc")
async def btc( interaction: discord.Interaction ):
      # if price > past_price:
      #   await interaction.response.send_message("Le prix du Bitcoin a augmenté depuis les dernières heures")
      # elif price < past_price:
       #  await interaction.response.send_message("Le prix du Bitcoin a diminué depuis les dernières heures")
       #else:
      #   await interaction.response.send_message("Le prix du Bitcoin n'a pas changé depuis les dernières heures")
       await interaction.response.send_message(price)        


client.run(token)