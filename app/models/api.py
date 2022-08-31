from woocommerce import API

wcapi = API(
    url="http://localhost/wordpress", # Your store URL
    consumer_key="ck_8b1f24fe6a781734957927a1a9e332a406bccffa", # Your consumer key
    consumer_secret="cs_782f092d97c706923b312420e0d064c66c0a9f19", # Sempre trocar saporra
    wp_api=True, # Enable the WP REST API integration
    version="wc/v3" # WooCommerce WP REST API version
)
retorno = wcapi.get("products", params={"per_page": 20}).json()
