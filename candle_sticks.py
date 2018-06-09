from settings import auth_client, product
import time, sqlite3
from datetime import datetime

endtime = time.time() + 60
while time.time() < endtime:
    value = datetime.utcnow().strftime("%S")
    entTime = int(value)
    print(60 - entTime)
    time.sleep(1)
    if entTime == 0 or entTime == 1:
        break

conn = sqlite3.connect('crypto_scalper.db')
c = conn.cursor()
stack = []

class Candle(object):

    def candleStick(self):
        while float(datetime.utcnow().strftime("%S.%f")) > 0:
            x = []
            init_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M")

            while init_time == datetime.utcnow().strftime("%Y-%m-%d %H:%M"):

                y = float(auth_client.get_product_ticker(product)['price'])
                print('*****API*****candle.py - Product Ticker: ', ticker_price)
                x.append(y)
                time.sleep(1)
                print(float(datetime.utcnow().strftime("%S.%f")))

            timex = float((datetime.utcnow() - datetime(1970,1,1)).total_seconds())
            c.execute(
                "CREATE TABLE IF NOT EXISTS candleSticks (id integer primary key autoincrement, product Text, candle_time TEXT, candle_low REAL, candle_high REAL, candle_open REAL, candle_close REAL )"
            )

            c.execute("INSERT INTO candleSticks ( candle_time, product, candle_low, candle_high, candle_open, candle_close) VALUES (?,?, ?, ?, ?, ?)",
                      (timex, product,  min(x), max(x), x[0], x[-1]))
            conn.commit()


            c.execute('SELECT * FROM candleSticks WHERE ID = (SELECT MAX(ID) FROM candleSticks) ')
            data = c.fetchall()
            for data in data:
                stack.append(list(data))
                print(stack[-5:])

