print("""You enter a dark room with two doors
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake")
    print("2. Scream at the bear")
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off.  Good Job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good Job!")
    else:
        print(f"Well, doing {bear} is probably beter.")
        print("Bear runs away.")
        
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. You flee.")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
        
    else:
        print("You go back and walk into town")
        print("1. You go to a bar and order a drink")
        print("2. You go into a blacksmith shop and buy a new sword")
        print("3. You go to a restaurant and order some food")
       
        flee = input("> ")
        
        if flee == "1":
            print("The drink was really poison and you died.  Good job!")
        
        elif flee == "2":
            print("The Blacksmith kills you for trying to use fake money.  Good job!")
        
        else:
            print("The food you ordered had poison and kills you.  Good job!")
   
   
else:
    print("you stumble around and fall on a knife and die.  Good job!")