def teamData(data) :
    data = data.split(",")
    return [ data[0] , { "points" : 3 * int(data[1]) + int(data[3]) } , { "gd" : int(data[4]) - int(data[5]) } ]

def createScoreBoard(SCOREBOARD,TEAMDATA) :
    if len(SCOREBOARD) == 0 :
        SCOREBOARD[0] = TEAMDATA
    else :
        rank = 0
        while  rank < len(SCOREBOARD) and SCOREBOARD[rank][1]["points"] > TEAMDATA[1]["points"] :
            rank += 1

        while rank < len(SCOREBOARD) and  SCOREBOARD[rank][2]["gd"] > TEAMDATA[2]["gd"] :

            if SCOREBOARD[rank][1]["points"] == TEAMDATA[1]["points"] :
                rank += 1
            else :
                break

        if rank == 0 :

            for temp in range(len(SCOREBOARD),0,-1) :
                SCOREBOARD[temp] = SCOREBOARD[temp-1]

            SCOREBOARD[0] = TEAMDATA

        elif rank == len(SCOREBOARD) :
            SCOREBOARD[rank] = TEAMDATA

        else :
            for temp in range(len(SCOREBOARD),-1,-1) :

                if temp > rank :
                    SCOREBOARD[temp] = SCOREBOARD[temp-1]
                elif temp == rank :
                    SCOREBOARD[rank] = TEAMDATA
                    break
                
    return SCOREBOARD

teamList = input("Enter Input : ").split("/")

SCOREBOARD = {}

for team in teamList :
    TEAMDATA = teamData(team)
    SCOREBOARD = createScoreBoard(SCOREBOARD,TEAMDATA)

print("== results ==")
for rank in range(len(SCOREBOARD)) :
    print(SCOREBOARD[rank])