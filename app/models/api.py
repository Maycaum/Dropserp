from socket import timeout
from woocommerce import API

wcapi = API(
    url="http://localhost/wordpress", # Your store URL
    consumer_key="ck_26551b40eae612cf26c7ce14b705e070c9956675", # Api allef
    consumer_secret="cs_a822e7ebf5a80fd1df8a82959876469d490ff317", # Sempre trocar saporra
    wp_api=True, # Enable the WP REST API integration
    version="wc/v3" # WooCommerce WP REST API version
)
