def water():
    strength = input("起こし方を選んでください\nhigh,middle,low\n")
    match strength:
        case "high":
            high()
        case "middle":
            middle()
        case "low":
            low()

def high():
    print("water high")
    
def middle():
    print("water middle")
    
def low():
    print("water low")