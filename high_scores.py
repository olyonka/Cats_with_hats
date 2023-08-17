import csv

def read_game_scores(filename):
    player_scores = {}

    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header

        for row in csvreader:
            player = row[0]
            score = int(row[1])
            player_scores.setdefault(player, []).append(score)

    return player_scores

def calculate_highest_scores(player_scores):
    highest_scores = {}

    for player, scores in player_scores.items():
        highest_scores[player] = max(scores)

    return highest_scores

def save_high_scores_to_csv(highest_scores):
    with open('high_scores.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Player name', 'Highest score'])

        sorted_scores = sorted(highest_scores.items(), key=lambda x: x[1], reverse=True)
        for player, score in sorted_scores:
            csvwriter.writerow([player, score])

def main():
    game_scores_filename = 'game_scores.csv'
    player_scores = read_game_scores(game_scores_filename)
    highest_scores = calculate_highest_scores(player_scores)
    save_high_scores_to_csv(highest_scores)

    print("High scores saved to high_scores.csv.")

if __name__ == "__main__":
    main()