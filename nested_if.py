sport = "basketball"
p1_score = 10
p2_score = 9

if sport.lower() == "golf":
    if p1_score == p2_score:
        print("It's a draw!")
    elif p1_score < p2_score:
        print("P1 wins")
    else:
        print("P2 wins")
elif sport.lower() == "basketball":
    if p1_score == p2_score:
        print("It's a draw!")
    elif p1_score > p2_score:
        print("P1 wins")
    else:
        print("P2 wins")
else:
    print("Unknown sport!")
