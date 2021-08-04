import time
import schedule

from reptile import index
from email import sends


def init1():
    msg = index.get_weather('101181001')
    msg = msg + '\n' +  index.get_movie()
    sends.send_email(msg)
    
init1()
# def run(coroutine):
#     try:
#         coroutine.send(None)
#     except StopIteration as e:
#         return e.value

# schedule.every().day.at('09:14').do(init1)

# while True:
#     schedule.run_pending()

#     time.sleep(3)