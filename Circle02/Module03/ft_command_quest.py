import sys


def command_quest() -> None:
    args = sys.argv
    argument = len(args) - (len(args) - 1)
    print(f"Program name: {args[0]}")
    if len(args) - 1 >= 1:
        print(f"Arguments received: {len(args) - 1}")
    else:
        print("No arguments provided!")
    while argument < len(args):
        print(f"Argument {argument}: {args[argument]}")
        argument += 1
    print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    command_quest()
