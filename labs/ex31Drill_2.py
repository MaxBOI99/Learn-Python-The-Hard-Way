print("""You enter a dark cave, the cave branches off to two other caves
which cave should you go into, Cave 1 or Cave 2?""")

cave = input("> ")

if cave == "1":
    print("There is a dungeon and a mysterious wall.")
    print("What do you do?")
    print("1. Open the dungeon")
    print("2. Lean against the wall and wait")
    
    dungeon = input("> ")
    
    if dungeon == "1":
        print("You enter a the dungeon and immediatly get trapped and die of starvation.")
    elif dungeon == "2":
        print("As you lean against the wall, a secret trap activates and kills you.")
    else:
        print("You die from the toxic fumes in the cave.")
    
        
elif cave == "2":
    print("You see a dim light at the end of the cave.")
    print("1. You go on.")
    print("2. Go go back home.")
  
    
    light = input("> ")
    
    if light == "1":
       
        print("At the end of the cave you see a big hole dimly lit by iridescent flowers.")
        print("You fall in and splash into an underground pond.")
        print("You see some ancient ruins on the other side of the cave")
        print("1. Swim across the pond and enter the ruins")
        print("2. Look around for an exit")
        
        
        pond = input("> ")
        
        if pond == "1":
            print("Theres a trap that immediately kills you")
            
        elif pond == "2":
            print("you find a small staircase that leads upward")
            print("you go up the stairs")
            print("you find yourself at the beginning and decide to go home")
        
        else:
            print("you get tired and cant swim and drown")
            
    elif light == "2":
        print("you go home and cry in the corner")
   
   
    else:
        print("you die of the toxic fumes in the cave.")
        
else:
    ("you die of toxic fumes in the cave.")