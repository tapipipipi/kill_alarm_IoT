#各フォルダに移動するためのインポート文
from light import light
from water import water
from vibrasion import vibration
from blow import blow
from sound import sound


payload = input("起こし方を選んでください\nlight,water,vibration,blow,sound\n")
print()

match payload:
    case "light":   #光
        light.light()
    
    case "water":   #水
        water.water()
        
    case "vibration":   #振
        vibration.vibration()
        
    case "blow":    #打
        blow.blow()
    
    case "sound":   #音
        sound.sound()

# payload_data = ["light","water","vibration","blow","sound"]
# strength_data = ["high","middle","low"]