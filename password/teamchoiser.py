import random

player1 = ["Mark Zuckerberg", "Bill Gates", "Larry Page", "Chad Hurley"]


teamA = []
teamB = []

while len(player1) > 0:
    
    playerA = random.choice(player1)
    
    teamA.append(playerA)
    
    player1.remove(playerA)
    

        
    
    
    playerB = random.choice(player1)
    
    teamB.append(playerB)
    
    player1.remove(playerB)
    
    
    print('TEAM A' , teamA)
    print('TEAM B' , teamBCD)

   