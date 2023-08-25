#各フォルダに移動するためのインポート文
from light import light
from water import water
from vibrasion import vibration
from blow import blow
from sound import sound

payload = input("起こし方を選んでください\nlight,water,vibration,blow,sound\n")
#print()

#def call_payload(payload):
if payload == "light":
        light.light()
elif payload == "water":
        water.water()
elif payload == "vibration":
        vibration.vibration()
elif payload == "blow":
        blow.blow()
elif payload == "sound":
        sound.sound()

# payload_data = ["light","water","vibration","blow","sound"]
# strength_data = ["high","middle","low"]