AmazonStockTrackr est un bot automatisé conçu pour surveiller la disponibilité et le prix de produits sur Amazon, et envoyer des alertes en temps réel via Telegram. Il permet aux passionnés de ne plus manquer les sorties ou les bonnes affaires sur leurs articles préférés.

Fonctionnalités principales
- Surveillance automatique des produits Pokémon sur Amazon.
- Alertes Telegram instantanées lorsque les produits sont en stock et vendus par Amazon.
- Contrôle du délai entre chaque vérification pour optimiser l’utilisation des API.
- Support multi-produits avec gestion personnalisée des seuils de prix (optionnel).

Prérequis
- Python 3.9 ou supérieur
- Clé API ScraperAPI (pour contourner les restrictions Amazon)
- Bot Telegram avec token d’accès
- Librairies Python : requests, python-telegram-bot, beautifulsoup4

Installation
- Clonez ce dépôt :
git clone https://github.com/fullya99/AmazonStockTrackr.git

cd AmazonStockTrackr

- Installez les dépendances :
pip install requests python-telegram-bot beautifulsoup4

Configurez vos clés dans le fichier config.py :

SCRAPERAPI_KEY = "votre_cle_scraperapi" TELEGRAM_BOT_TOKEN = "votre_token_telegram" TELEGRAM_CHAT_ID = "votre_chat_id"

Ajoutez les URLs des produits Pokémon à suivre dans main.py.

Utilisation

Lancez le bot avec la commande :

python main.py

Le bot vérifiera périodiquement la disponibilité et le prix des produits listés, et vous enverra une notification Telegram dès qu’un produit est disponible et vendu par Amazon.

Personnalisation
- Modifiez l’intervalle de vérification dans config.py (CHECK_INTERVAL_SECONDS).
- Ajoutez des critères de prix pour recevoir des alertes uniquement en dessous d’un certain seuil.
- Personnalisez les messages Telegram dans messages.py.

Limitations et avertissements
- Le bot utilise ScraperAPI pour éviter les blocages, mais un usage intensif peut entraîner des limitations.
- Amazon peut modifier la structure de ses pages, ce qui peut nécessiter une mise à jour du parsing HTML.
- L’utilisation du bot doit respecter les conditions d’utilisation d’Amazon.
- Ce bot ne réalise pas d’achats automatiques.

Contribution

- Les contributions sont les bienvenues ! N’hésitez pas à ouvrir une issue ou une pull request.

Licence

- Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
