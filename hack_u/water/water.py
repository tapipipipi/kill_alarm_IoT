from threading import Thread    #起動時間を並列で作動させるモジュール
import pigpio # pigpioモジュールを使用
import time #時間数えるモジュール
#以下、ピン番号をインポートするモジュール
from IoT_setting import gpio_sw_in
from IoT_setting import gpio_sw_led
from IoT_setting import gpio_morter
from IoT_setting import gpio_valve

timer = True
def water():
    global timer
    
    #pigpioの準備
    pi = pigpio.pi()
    
    # ピンを出力に設定
    pi.set_mode(gpio_morter,pigpio.OUTPUT)  #圧縮モーター
    pi.set_mode(gpio_sw_led,pigpio.OUTPUT)  #LED_SW
    pi.set_mode(gpio_valve,pigpio.OUTPUT)   #水発射バルブ

    # スイッチピンを入力、プルアップに設定
    pi.set_mode(gpio_sw_in,pigpio.INPUT)
    pi.set_pull_up_down(gpio_sw_in,pigpio.PUD_UP)
    
    # スイッチの状態を取得
    sw = pi.read(gpio_sw_in)

    timer = True
    #30秒後にoffにするタイマー
    def control_timer():
        global timer
        time.sleep(30)
        timer = False   

    #タイマースタート
    thread = Thread(target=control_timer)
    thread.start()
    pi.write(gpio_sw_led,1)     # LED_SW点灯
    while timer:
        pi.write(gpio_morter,1)     # 水圧縮
        print("charge")
        time.sleep(1)
        pi.write(gpio_morter,1)     #水発射
        print("open")
        time.sleep(0.2)             # 0.2秒待機
        pi.write(gpio_morter,0)     # 水停止
        print("close")
        if sw == 0:                 #スイッチを押した場合止まる
            break

    pi.write(gpio_sw_led,0)         # LED_SW消灯
    print("Lsw_off")   
    #pigpioから切断
    pi.stop()