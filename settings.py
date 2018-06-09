import gdax

passphrase = ""
key = ""
b64secret = ""
auth_client = gdax.AuthenticatedClient(key, b64secret, passphrase)
maxTrades = 1
open_trade_time_limit = 1
minimum_order_fill_time = 1
limit_entry_point_diff = 1
product = ''

