def sound():
    strength = input("起こし方を選んでください\nhigh,middle,low\n")
    match strength:
        case "high":
            high()
        case "middle":
            middle()
        case "low":
            low()

def high():
    print("sound high")
    
def middle():
    print("sound middle")
    
def low():
    print("sound low")