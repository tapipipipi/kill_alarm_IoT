import time
from threading import Thread

timer = True
def water():
    # #pin番号
    # gpio = 10
    
    # #pigpioの準備
    # pi = "pigpio.pi()"
    
    # # 蛇口ピンを出力に設定
    # pi.set_mode(gpio,"pigpio.OUTPUT")

    # # スイッチピンを入力、プルアップに設定
    # pi.set_mode("pigpio".INPUT)
    # pi.set_pull_up_down("pigpio.PUD_UP")

    #pi.write(gpio,1)        # 水発射
    print("on")
    time.sleep(0.2)     # time秒待機
    #pi.write(gpio,0)        # 水停止
    print("off")
    print("succes")
    # # pigpioから切断
    # pi.stop()