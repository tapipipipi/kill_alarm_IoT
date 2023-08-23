def light():
    strength = input("起こし方を選んでください\nhigh,middle,low\n")
    match strength:
        case "high":
            high()
        case "middle":
            middle()
        case "low":
            low()

def high():
    print("light high")
    
def middle():
    print("light middle")
    
def low():
    print("light low")