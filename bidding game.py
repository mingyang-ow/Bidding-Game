
from click import clear

global endofbid
endofbid = False
information = {}

def highestbid():
    highest = 0
    winner = ""
    for bid in information:
        amount = information[bid]
        if amount > highest:
            highest = amount
            winner = bid
    print(f"The winner is {winner}, at {highest}")
    exit()
    
            
            
        

while not endofbid:
    name = input("What is your name? ")
    value = int(input("What is your bet? "))
    information[name] = value
    cont = input("Are there any other bidders? ").lower()
    if cont == "no":
        endofbid is True
        highestbid()
    elif cont == "yes":
        clear()

