# Advent Of Code 2022
# Day 2 - Rock Paper Scissors
#
# PJD

def rock_paper_scissor_shoot(player1, player2):
    outcome = ""
    if player1 == player2:
        outcome = "Draw"
    elif player1 == "Rock":
        if player2 == "Paper":
            outcome = "Win"
        elif player2 == "Scissor":
            outcome = "Loss"
    elif player1 == "Paper":
        if player2 == "Scissor":
            outcome = "Win"
        elif player2 == "Rock":
            outcome = "Loss"
    elif player1 == "Scissor":
        if player2 == "Rock":
            outcome = "Win"
        elif player2 == "Paper":
            outcome = "Loss"
    return outcome


def new_strategy_play(player1, outcome):
    player2 = ""
    if outcome == "Lose":
        if player1 == "Rock":
            player2 = "Scissor"
        elif player1 == "Paper":
            player2 = "Rock"
        elif player1 == "Scissor":
            player2 = "Paper"
    elif outcome == "Win":
        if player1 == "Rock":
            player2 = "Paper"
        elif player1 == "Paper":
            player2 = "Scissor"
        elif player1 == "Scissor":
            player2 = "Rock"
    elif outcome == "Draw":
        player2 = player1

    return player2


if __name__ == '__main__':
    scoring_values = {"Rock": 1, "Paper": 2, "Scissor": 3, "Loss": 0, "Draw": 3, "Win": 6}
    letter_to_choice_opponent = {"A": "Rock", "B": "Paper", "C": "Scissor"}
    letter_to_choice_you = {"X": "Rock", "Y": "Paper", "Z": "Scissor"}

    total_score = 0
    input_data = []
    result = ""

    with open("day2_input.txt") as f:
        input_data = f.readlines()

# Part 1 - Total Score using strategy
    for data in input_data:
        current_round = data.strip().split(" ")

        opponent = letter_to_choice_opponent[current_round[0]]
        you = letter_to_choice_you[current_round[1]]

        result = rock_paper_scissor_shoot(opponent, you)

        total_score = total_score + scoring_values[you] + scoring_values[result]

    print("Total Score = {0}".format(total_score))

# Part 2 -
    letter_to_outcome = {"X": "Lose", "Y": "Draw", "Z": "Win"}
    total_score = 0

    for data in input_data:
        current_round = data.strip().split(" ")

        opponent = letter_to_choice_opponent[current_round[0]]
        you = letter_to_outcome[current_round[1]]

        you = new_strategy_play(opponent, you)

        result = rock_paper_scissor_shoot(opponent, you)

        total_score = total_score + scoring_values[you] + scoring_values[result]

    print("Total Score = {0}".format(total_score))






