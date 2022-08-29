from woocommerce import API

wcapi = API(
    url="http://localhost/wordpress", # Your store URL
    consumer_key="ck_011cbc9209f2ed35b537f1c2b3ef37f877bd8e90", # Your consumer key
    consumer_secret="cs_12cc3095ad780110f028411e6a23353dc028c12a", # Sempre trocar saporra
    wp_api=True, # Enable the WP REST API integration
    version="wc/v3" # WooCommerce WP REST API version
)
retorno = wcapi.get("products", params={"per_page": 20}).json()
