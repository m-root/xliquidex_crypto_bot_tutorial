from settings import auth_client, product


class Ticker(object):

    def ticker(self):
        ticker = auth_client.get_product_ticker(product)
        tickerx = ticker['price']
        tickerx = float(tickerx)
        tickerTime = ticker['time']
        print('{}  {}'.format(tickerTime, tickerx))
        return tickerx