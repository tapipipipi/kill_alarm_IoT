import time
from threading import Thread

timer = True

def f():
    global timer
    time.sleep(5)
    timer = False

thread = Thread(target=f)
thread.start()
while timer:
    print("on")         # LED点灯
    time.sleep(0.5)     # time秒待機
    print("off")        # LED消灯
    time.sleep(0.5)     # time秒待機