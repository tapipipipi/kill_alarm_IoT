def vibration():
    strength = input("起こし方を選んでください\nhigh,middle,low\n")
    match strength:
        case "high":
            high()
        case "middle":
            middle()
        case "low":
            low()

def high():
    print("vibration high")
    
def middle():
    print("vibration middle")
    
def low():
    print("vibration low")