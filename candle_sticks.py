from settings import auth_client, product
import time, sqlite3
from datetime import datetime

currentTime = datetime.utcnow().strftime("%Y-%m-%d %H:%M")
while currentTime == datetime.utcnow().strftime("%Y-%m-%d %H:%M"):
    print(60 - int(datetime.utcnow().strftime("%S")))
    time.sleep(1)

conn = sqlite3.connect('xliquidex.db')
c = conn.cursor()
stack = []

class Candle(object):

    def candleStick(self):
        while float(datetime.utcnow().strftime("%S.%f")) > 0:
            x = []
            a = []
            init_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M")
            while init_time == datetime.utcnow().strftime("%Y-%m-%d %H:%M"):
                y = float(auth_client.get_product_ticker(product)['price'])
                x.append(y)
                b = float(auth_client.get_product_ticker(product)['size'])
                a.append(b)
                time.sleep(1)
                print(float(datetime.utcnow().strftime("%S.%f")))
            timex = float((datetime.utcnow() - datetime(1970,1,1)).total_seconds())
            c.execute(
                "CREATE TABLE IF NOT EXISTS candleSticks (id integer primary key autoincrement, product Text, candle_time TEXT, candle_low REAL, candle_high REAL, candle_open REAL, candle_close REAL )"
            )

            c.execute("INSERT INTO candleSticks ( candle_time, product, candle_low, candle_high, candle_open, candle_close, volume) VALUES (?,?, ?, ?, ?, ?, ?)",
                      (timex, product,  min(x), max(x), x[0], x[-1], sum(a) ))
            conn.commit()

            c.execute('SELECT * FROM candleSticks WHERE ID = (SELECT MAX(ID) FROM candleSticks) ')
            data = c.fetchall()
            for data in data:
                stack.append(list(data))
                print(stack[-5:])
