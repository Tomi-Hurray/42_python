import sys


def get_no_args() -> int:
    no_args = len(sys.argv)
    return no_args


def score_analyzer() -> None:
    args = sys.argv
    no_args = get_no_args()
    scores = []
    for i in range(1, (no_args)):
        try:
            scores.append(int(args[i]))
        except ValueError:
            print(f"Invalid parameter: '{args[i]}'")
    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Average score: {(sum(scores) / len(scores))}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    score_analyzer()
