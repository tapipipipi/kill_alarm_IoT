def blow():
    strength = input("起こし方を選んでください\nhigh,middle,low\n")
    match strength:
        case "high":
            high()
        case "middle":
            middle()
        case "low":
            low()

def high():
    print("blow high")
    
def middle():
    print("blow middle")
    
def low():
    print("blow low")