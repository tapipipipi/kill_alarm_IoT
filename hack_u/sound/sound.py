from threading import Thread    #起動時間を並列で作動させるモジュール
import pigpio # pigpioモジュールを使用
import time #時間数えるモジュール
#以下、ピン番号をインポートするモジュール
from IoT_setting import gpio_sw_in
from IoT_setting import gpio_sw_led
from IoT_setting import gpio_led

timer = True
def sound():
    global timer
    
    #pigpioの準備
    pi = pigpio.pi()
    
    # ピンを出力に設定
    pi.set_mode(gpio_led,pigpio.OUTPUT)  
    pi.set_mode(gpio_sw_led,pigpio.OUTPUT)  #LED_SW

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
        pi.write(gpio_led,1)        # LED点灯
        print("on")
        time.sleep(0.5)     # time秒待機
        pi.write(gpio_led,0)        # LED消灯
        print("off")
        time.sleep(0.5)     # time秒待機
        if sw == 0:                 #スイッチを押した場合止まる
            break

    pi.write(gpio_led,0)        # LED消灯
    pi.write(gpio_sw_led,0)         # LED_SW消灯
    print("Lsw_off")   
    #pigpioから切断
    pi.stop()