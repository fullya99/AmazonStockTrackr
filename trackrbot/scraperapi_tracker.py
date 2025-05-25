
import requests
from bs4 import BeautifulSoup

class ScraperAPIClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_product_html(self, product_url):
        api_url = f"http://api.scraperapi.com?api_key={self.api_key}&url={product_url}&country_code=fr"
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception(f"Erreur ScraperAPI: {response.status_code}")

def parse_amazon_product_page(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Prix
    price = None
    price_selectors = [
        '#priceblock_ourprice',
        '#priceblock_dealprice',
        '#priceblock_saleprice',
        '.a-price .a-offscreen',
        '#tp_price_block_total_price_ww',
        '#newBuyBoxPrice',
        '.offer-price',
    ]
    for selector in price_selectors:
        price_tag = soup.select_one(selector)
        if price_tag and price_tag.text.strip():
            price_text = price_tag.text.strip().replace('\xa0', ' ').replace('€', '').replace(',', '.').strip()
            try:
                price = float(price_text)
                break
            except:
                continue

    # Disponibilité
    availability = None
    add_to_cart_button = soup.select_one('#add-to-cart-button')
    buy_now_button = soup.select_one('#buy-now-button')
    if add_to_cart_button or buy_now_button:
        availability = 'en stock'
    else:
        unavailable_text = soup.find(text=lambda t: t and 'actuellement indisponible' in t.lower())
        if unavailable_text:
            availability = 'indisponible'

    # Vendeur (vendu et expédié par Amazon)
    seller = None
    seller_tag = soup.select_one('#merchant-info')
    if seller_tag:
        seller_text = seller_tag.text.strip().lower()
        if 'vendu par amazon' in seller_text and 'expédié par amazon' in seller_text:
            seller = 'amazon'
        else:
            seller = seller_text
    else:
        seller_alt = soup.find(text=lambda t: t and 'vendu par amazon' in t.lower())
        if seller_alt:
            seller = 'amazon'

    return price, availability, seller
