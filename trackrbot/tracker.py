import time
from trackrbot.scraperapi_tracker import ScraperAPIClient, parse_amazon_product_page
from trackrbot.alerts import send_telegram_alert

class ProductTracker:
    def __init__(self, scraperapi_key, telegram_bot_token, telegram_chat_id):
        self.scraperapi_client = ScraperAPIClient(scraperapi_key)
        self.telegram_bot_token = telegram_bot_token
        self.telegram_chat_id = telegram_chat_id

    def track_product(self, product):
        try:
            html = self.scraperapi_client.fetch_product_html(product.url)
            price, availability, seller = parse_amazon_product_page(html)
            print(f"Prix: {price}, Disponibilité: {availability}, Vendeur: {seller}")
            if availability == 'en stock' and seller == 'amazon':
                message = f"🚨 Le produit est en stock et vendu par Amazon !\n{product.url}"
                send_telegram_alert(self.telegram_bot_token, self.telegram_chat_id, message)
                return True
            print("Produit non disponible ou conditions non remplies.")
            return False
        except Exception as e:
            print(f"Erreur lors du suivi produit: {e}")
            return False

    def start_tracking(self, products, check_interval=600):
        print("Démarrage du suivi multi-produits...")
        while True:
            for product in products:
                self.track_product(product)
            time.sleep(check_interval)