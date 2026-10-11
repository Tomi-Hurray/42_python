import random

if __name__ == "__main__":
    names_list = ['alice', 'bob', 'charlie', 'dylan', 'emma', 'gregory',
                  'john', 'kevin', 'liam']

    initial_list = [name.capitalize() if random.randint(0, 1) == 1 else name
                    for name in names_list]

    print(f"Initial list of players: {initial_list}")
    capitalized_names = [x.capitalize() if x.istitle() is False else x for x
                         in initial_list]
    print(f"New list with all names capitalized {capitalized_names}")
    capitalized_only = [y for y in initial_list if y.istitle()]
    print(f"New list of capitalized names only {capitalized_only}")
    if capitalized_only:
        score_dict = {v: random.randint(0, 1000) for v in capitalized_only}
        print(f"Score dict: {score_dict}")
        scores = tuple(z for z in score_dict.values())
        avg_score = round(sum(scores, 0) / len(scores))
        print(f"Score average is: {avg_score}")
        high_scores = {player: score for player, score in score_dict.items()
                       if score > avg_score}
    else:
        print("Empty dataset")
    print(f"High scores: {high_scores}")
