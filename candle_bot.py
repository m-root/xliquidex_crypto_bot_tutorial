from candle_sticks import Candle
from datetime import datetime
import time


def restart():
    while True:
        try:
            candle = Candle()
            candle.candleStick()

        except Exception as e:
            print(e)
            time.sleep(1)

        time.sleep(1)


if __name__ == '__main__':
    restart()
