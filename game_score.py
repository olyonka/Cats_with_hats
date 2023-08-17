import random
import csv

def simulate_game(player_names, rounds):
    player_scores = {}

    for player in player_names:
        scores = [random.randint(0, 1000) for _ in range(rounds)]
        player_scores[player] = scores

    return player_scores

def save_to_csv(data):
    with open('game_scores.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Player name', 'Score'])

        for player, scores in data.items():
            for score in scores:
                csvwriter.writerow([player, score])

def main():
    player_names = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
    rounds = 100

    player_scores = simulate_game(player_names, rounds)
    save_to_csv(player_scores)

    print("Game scores saved to game_scores.csv.")

if __name__ == "__main__":
    main()
