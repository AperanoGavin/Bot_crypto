import discord
import io
import requests
import time
from discord import app_commands
from binance.client import Client
from dotenv import load_dotenv
load_dotenv()
import os
token = os.getenv("TOKEN")

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
GUILD = os.getenv('1047812022789734480')
#intents = discord.Intents.default()
#intents.message_content = True
       

# Seuils de prix définis dans votre stratégie
buy_threshold = 1000
sell_threshold = 1100

# Quantité de cryptomonnaie à acheter ou vendre
order_size = 0.1

# ID de produit de Binance (par exemple, BTCUSDT pour le Bitcoin en dollars américains)
product_id = 'BTCUSDT'

# Créer un objet Client avec vos clés d'API et votre mot de passe de sécurité
client = Client(api_key, api_secret, passphrase)



client.run(token)