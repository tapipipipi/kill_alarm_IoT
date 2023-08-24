import time
from threading import Thread
#from datetime import datetime

timer = True
def vibration_contlall(interval):
    # #pin番号
    # gpio = 10
    
    # #pigpioの準備
    # pi = "pigpio.pi()"
    
    # # 振動ピンを出力に設定
    # pi.set_mode(gpio,"pigpio.OUTPUT")

    # # スイッチピンを入力、プルアップに設定
    # pi.set_mode("pigpio".INPUT)
    # pi.set_pull_up_down("pigpio.PUD_UP")
    
    
    #30秒後にoffにするタイマー
    def control_timer():
        global timer
        time.sleep(30)
        timer = False

    #タイマースタート
    thread = Thread(target=control_timer)
    thread.start()
    while timer:
        #pi.write(gpio,1)        # 振動開始
        print("on")
        time.sleep(interval)     # time秒待機
        #pi.write(gpio,0)        # 振動終了
        print("off")
        time.sleep(interval)     # time秒待機

    #pi.write(gpio,0)        # 振動終了
    print("off")
    print("succes")
    # # pigpioから切断
    # pi.stop()

def vibration():
    strength = input("強さを選んでください\nhigh,middle,low\n")
    match strength:
        case "high":
            vibration_contlall(0.5) #0.5秒間隔
        case "middle":
            vibration_contlall(1.5) #1秒感覚
        case "low":
            vibration_contlall(3) #3秒感覚