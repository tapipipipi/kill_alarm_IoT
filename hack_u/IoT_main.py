#サーバーから受け取るファイル
import websocket
import json
import time
import schedule
import threading
from IoT_base import call_payload

timer_tag = "timer_data"
timer_datas = {}

#タイマーを削除する
def clear_timer():
    schedule.clear(timer_tag)

def add_timer(timer_data):
    pass

def test_print():
    print("hello")

device_data = {
    "deviceToken": "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJkZXZpY2VpZCI6IjQ0YTg1YTU5MDZmMjdhZDRiZTAwZjI0MGRlZGJjYzcxMmYyYTlkYmE2NDIzZWZhODlhNDYwN2E1MTJiZGUzZWQ1NDcxMDU4ODM5MGMzYjcxNGQ4MThhZTBmYmQ2ODljYWNjYWMyOTNmNDMyNGUxZmEzYTViZWUxNGQxODIyNDQxIiwidG9rZW5pZCI6ImZmZWNjODgwLTQyYzEtNGM2MS04MzdiLTRlZDY0MjVlOGQ1ZCJ9.dh64RuibpTQ2O17PAlfqrnXInF2ZE42weuckVeock4ROBjzhNVMdXOTekFShkAEpgomO2lCTkiMXh6ttB5Z1qg",
    "deviceid": "44a85a5906f27ad4be00f240dedbcc712f2a9dba6423efa89a4607a512bde3ed54710588390c3b714d818ae0fbd689caccac293f4324e1fa3a5bee14d1822441"
}

def timer_task(index):
    task_data = dict(timer_datas["timers"][index])
    
    for payload in task_data["payloads"]:
        payload_thread = threading.Thread(target=call_payload,args=(payload["payload_name"],))
        #payload_thread.setDaemon(True)
        payload_thread.start()

def do_wakeup(payloads):
    for payload in payloads:
        payload_thread = threading.Thread(target=call_payload,args=(payload["payload_name"],))
        #payload_thread.setDaemon(True)
        payload_thread.start()

def on_message(wsapp, message):
    global loop_connect,timer_datas

    print(message)
    load_dict = json.loads(message)

    match load_dict["msgcode"]:
        case "11110":
            loop_connect = False
        case "11143":
            do_wakeup(load_dict["payloads"])
        case "11142":
            timer_datas = load_dict

            clear_timer()
            for index,timer in enumerate(timer_datas["timers"]):
                if timer["enabled"]:
                    hour_string = timer["call_hour"]
                    min_string = timer["call_min"]

                    print(f"{hour_string}:{min_string}")
                    schedule.every().day.at(f"{hour_string}:{min_string}").do(timer_task,index = int(index)).tag(timer_tag)
def on_open(wsapp):
    print("Connected")
    auth_data = {
        "msgtype": 'authToken',
        "token" : device_data["deviceToken"]
    }

    wsapp.send(json.dumps(auth_data))

loop_connect = True

def connect_server():
    global loop_connect
    while loop_connect:
        wsapp = websocket.WebSocketApp("ws://tidalhip.local:8000/iotws", on_message=on_message,on_open=on_open)

        wsapp.run_forever()
        
        wsapp.close()

        if not loop_connect:
            break

        print("reconnect")

        time.sleep(3)

if __name__ == "__main__":
    server_thread = threading.Thread(target=connect_server)

    server_thread.start()
    
    while True:
        schedule.run_pending()
        time.sleep(1)