choices_points = {"rock": 1, "paper": 2, "scissors": 3}

map_p1 = {"A": "rock", "B": "paper", "C": "scissors"}
map_p2 = {"X": "lose", "Y": "draw", "Z": "win"}

outcome = {"win":6 , "draw":3, "lose":0}



def guess_play(p1,outcome):
    #return play for p2 in order to get outcome
    if(outcome == "draw"):
        return p1
    elif(outcome == "win"):
        if(p1 == "rock"):
            return "paper"
        elif(p1 == "scissors"):
            return "rock"
        elif(p1 == "paper"):
            return "scissors"
    else:
        if(p1 == "rock"):
            return "scissors"
        elif(p1 == "scissors"):
            return "paper"
        elif(p1 == "paper"):
            return "rock"
    



def calculate_winner(p1,p2):
    #return points for p1
    if(p1 == p2):
        return outcome["draw"] + choices_points[p1]
    elif(p1 == "rock" and p2 == "scissors"):
        return outcome["win"] + choices_points[p1]
    elif(p1 == "scissors" and p2 == "paper"):
        return outcome["win"] + choices_points[p1]
    elif(p1 == "paper" and p2 == "rock"):
        return outcome["win"] + choices_points[p1]
    else:
        return outcome["lose"] + choices_points[p1]

def main():
    total_points = 0
    with open("input.txt","r") as f:
        for rline in f:
            line = rline.strip()
            #need to swap p1 and p2 because we are calculating p2's points
            p2_play = guess_play(map_p1[line[0]],map_p2[line[2]])
            # print(p2_play)
            total_points += calculate_winner(p2 = map_p1[line[0]],p1 = p2_play)
            # print(total_points)
    print(total_points)

main()