import random
import time

def player_total_compartments(number_of_players: int):               #player counting
    player_list = []

    for i in range(number_of_players):
        player_scores = {}
        player_name = input(f"Input player name {i + 1}: ")
        score = 0
        player_scores['name'] = player_name
        player_scores['score'] = score
        player_list.append(player_scores)

    return player_list                                      #returns a dictionary containing the player name and initial scores

def slow_print(text, delay =0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def match():                                                    #random number generation
    roll_score = 0
    print("Commencing dice roll...")

    
    while True:
        rand_score = random.randint(1,6)
        slow_print(f"You rolled a {rand_score}")

        if rand_score != 1:
            player_decide = input("Would you like to roll again (Y/N)? ")
            if player_decide == "Y" or player_decide == "y":
                roll_score += rand_score
                continue

            elif player_decide == "N" or player_decide == "n":
                roll_score += rand_score
                slow_print(f"Accumulated score for this round is {roll_score}")
                break
            else:
                print("Invalid input. Default decision to Y.")
                continue
         
        else:                                                   #player rolled a 1, accumulated score resets to 0.
            roll_score = 0
            slow_print("Accumulated score has been reset to 0.")
            break
    
    return roll_score

def rounds(player_score_initial):
    round_number = 1
    

    while True:
        slow_print(f"Round {round_number} --------------")

        for i in range(len(player_score_initial)):              #commences each round for all players
            print(f"Player {i+1} ({player_score_initial[i]['name']}'s) turn:")
            print(f"Current score: {player_score_initial[i]['score']} \n")
            added_score = match()
            player_score_initial[i]['score'] += added_score
            print(f"Score for Round {round_number}: {player_score_initial[i]['score']} \n")
        
        round_number += 1 
        winner_list = []

        for j in range(len(player_score_initial)):
            win_con = player_score_initial[j]['score'] 
            if win_con >= 50:                                   #change later (Win Con)
                winner_list.append(player_score_initial[j]['name'])

            if len(winner_list) > 0 and j + 1 == len(player_score_initial):
                return winner_list

def main():
    print("Welcome to Pig Game!")
    print("--------------------")
    number_of_players = int(input("Input number of players: "))

    player_score_initial = player_total_compartments(number_of_players)  #list containing dictionary containing score
    
    print("--------------------\n")
    print("Let's start the match!\n")

    winner = rounds(player_score_initial) 
    final_winner = ""

    slow_print("----------------------------------------------------------")
    slow_print("A score of 50 has been reached. A winner has been decided.")
    for index, value in enumerate(winner):
        final_winner += f"{value}"
        if index + 1 < len(winner):
            final_winner += ", "

    slow_print(f"Winner/s: {final_winner}")
    slow_print("----------------------------------------------------------")

main()
while True:
    choice = input("Press q to quit: ")
    if choice.lower() == 'q':
        break
