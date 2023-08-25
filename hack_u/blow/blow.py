from threading import Thread    #起動時間を並列で作動させるモジュール
import pigpio # pigpioモジュールを使用
import time #時間数えるモジュール
#以下、ピン番号をインポートするモジュール
from IoT_setting import gpio_sw_in 
from IoT_setting import gpio_sw_led
from IoT_setting import gpio_blow
from IoT_setting import gpio_sw_limit

#pigpioの準備
pi = pigpio.pi()
timer = True #タイマーを動作させる変数
#PWMパラメータ
duty1 = 2.5 #デューティー比を%で指定 0度はduty2.5%
duty2 = 12 #デューティー比を%で指定 180度はduty12%
freq = 50 #PWM周波数をHzで指定 SG90は1周期20ms(50Hz)

#パラメータ変換
cnv_dutycycle1 = int((duty1 * 1000000 / 100))
cnv_dutycycle2 = int((duty2 * 1000000 / 100))

def blow():
    global timer
    
    # 各ピンを出力に設定
    pi.set_mode(gpio_blow,pigpio.OUTPUT)
    pi.set_mode(gpio_sw_led,pigpio.OUTPUT) #LED_SW

    #スイッチピンを入力、プルアップに設定
    pi.set_mode(gpio_sw_in,pigpio.INPUT)
    pi.set_mode(gpio_sw_limit,pigpio.INPUT)
    pi.set_pull_up_down(gpio_sw_in,pigpio.PUD_UP)
    pi.set_pull_up_down(gpio_sw_limit,pigpio.PUD_UP)
    
    #スイッチの状態を取得
    sw_in = pi.read(gpio_sw_in)
    sw_limit = pi.read(gpio_sw_limit)
    
    timer = True
    #30秒後にoffにするタイマー
    def control_timer():
        global timer
        time.sleep(30)
        timer = False

    #タイマースタート
    thread = Thread(target=control_timer)
    thread.start()
    
    pi.write(gpio_sw_led,1)         # LED_SW点灯
    print("LED_SW点灯")
    while timer:
        pi.hardware_PWM(gpio_blow, freq, cnv_dutycycle1) #サーボを0度の位置に駆動
        print("standing by")
        print("Complete")
        pi.hardware_PWM(gpio_blow, freq, cnv_dutycycle2) #サーボを180度の位置に駆動"
        if sw_in == 0:              # スイッチを押した場合止まる
            break
    pi.set_servo_pulsewidth(gpio_blow, 500)
    pi.hardware_PWM(gpio_blow, freq, cnv_dutycycle1) #サーボを0度の位置に駆動
    print("end")
    pi.write(gpio_sw_led,0)         # LED消灯
    print("LED消灯")
    
    # pigpioから切断
    pi.stop()