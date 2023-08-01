pin = 1122
tr = 0

while tr < 3:
    inpin = input("PIN Code? ")
    if str(inpin) != str(pin):
        tr += 1
        if tr == 3:
            print("Your card is blocked.")
        else:
            print(f"Try again. Remain {3-tr} tries.") 
    else:
        print("Welcome to system.")
        tr = 3
