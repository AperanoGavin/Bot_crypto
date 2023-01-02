import time
from binance.client import Client

# Seuils de prix définis dans votre stratégie
buy_threshold = 1000
sell_threshold = 1100

# Quantité de cryptomonnaie à acheter ou vendre
order_size = 0.1

# ID de produit de Binance (par exemple, BTCUSDT pour le Bitcoin en dollars américains)
product_id = 'BTCUSDT'

# Créer un objet Client avec vos clés d'API et votre mot de passe de sécurité
client = Client(api_key, api_secret, passphrase)
