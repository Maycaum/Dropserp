from socket import timeout
from woocommerce import API

wcapi = API(
    url="http://localhost/wordpress", # Your store URL
    consumer_key="ck_821ae5885990e933baea78120de03032954ccf39", # Api allef
    consumer_secret="cs_8282a4332ac8067a070843ce9fa3c5e17fd2cc43", # Sempre trocar saporra
    wp_api=True, # Enable the WP REST API integration
    version="wc/v3" # WooCommerce WP REST API version
)
