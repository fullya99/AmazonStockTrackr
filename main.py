from trackrbot.product import Product
from trackrbot.tracker import ProductTracker

if __name__ == "__main__":
    scraperapi_key = "{Your_ScraperAPI_Key}"
    telegram_bot_token = "{Your_Bot_Token}"
    telegram_chat_id = "{Your_Chat_ID}"

    # On met price_threshold à None ou 0 car on ne veut pas filtrer sur le prix
    products = [
        Product(url="https://www.amazon.fr/Pok%C3%A9mon-JCC-Rivalités-entièrement-Accessoires/dp/B0F2QWXFYS?&linkCode=ll1&tag=arthurpsg-21&linkId=23fab50e569e3f099ec3751f7480ab91&language=fr_FR&ref_=as_li_ss_tl", price_threshold=0),
        Product(url="https://www.amazon.fr/Pok%C3%A9mon-boosters-Rivalités-Destinées-boosters/dp/B0F8BLHN4B?&linkCode=ll1&tag=arthurpsg-21&linkId=f6541c0012846f3384ed9c5fbdc95212&language=fr_FR&ref_=as_li_ss_tl", price_threshold=0),
        Product(url="https://www.amazon.fr/Pok%C3%A9mon-JCC-présentoir-Rivalités-Destinées/dp/B0F2QQM1JX?&linkCode=ll1&tag=arthurpsg-21&linkId=9e5a093ad76c4eed41abb7a20baa0b72&language=fr_FR&ref_=as_li_ss_tl", price_threshold=0),
        Product(url="https://www.amazon.fr/Pok%C3%A9mon-boosters-Rivalités-Destinées-Carte/dp/B0F555K42C?&linkCode=ll1&tag=arthurpsg-21&linkId=f6dfabee96e39966e20ac1b0b80c0348&language=fr_FR&ref_=as_li_ss_tl", price_threshold=0),
        Product(url="https://www.amazon.fr/Pok%C3%A9mon-boosters-Kangourex-Rivalités-Carte/dp/B0F54MS56J?ref_=ast_sto_dp", price_threshold=0),
    ]

    tracker = ProductTracker(scraperapi_key, telegram_bot_token, telegram_chat_id)
    tracker.start_tracking(products)