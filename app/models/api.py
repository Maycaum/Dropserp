from woocommerce import API

wcapi = API(
    url="http://localhost/wordpress", # Your store URL
    consumer_key="ck_ac58508f6ad402d87e1d9afbc7fc0b3d1a0fc0cc", # Your consumer key
    consumer_secret="cs_3ea445496ab3084cd235a6cfccf0d0e74878770f", # Your consumer secret
    wp_api=True, # Enable the WP REST API integration
    version="wc/v3" # WooCommerce WP REST API version
)
retorno = wcapi.get("products", params={"per_page": 20}).json()
