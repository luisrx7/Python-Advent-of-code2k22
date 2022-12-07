choices_points = {"rock": 1, "paper": 2, "scissors": 3}

map_p1 = {"A": "rock", "B": "paper", "C": "scissors"}
map_p2 = {"X": "rock", "Y": "paper", "Z": "scissors"}

outcome = {"win":6 , "draw":3, "lose":0}




def calculate_winner(p1,p2):
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
            total_points += calculate_winner(p2 = map_p1[line[0]],p1 = map_p2[line[2]])
    print(total_points)

main()