import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file = sys.argv[1]
        try:
            f = open(file, 'r')
            print(f"Error opening file: {file}")
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file {file}")
            print("- - -\n")
            print(f.read())
            print("\n- - -")
            f.close()
            print("File 'ancient_fragment.txt' closed.\n")
            print("Transform data:")
            print("- - -\n")
            f = open(file)
            transformed = []
            for line in f:
                line = line.rstrip('\n')
                line = line + '#'
                print(line)
                transformed.append(line)
            f.close()
            print("\n- - -")
            print("Enter new file name (or empty): ", end="", flush=True)
            d = sys.stdin.readline().strip()
            if d:
                print(f"Saving data to '{d}'")
                f2 = open(d, 'w')
                for line in transformed:
                    f2.write(line + '\n')
                f.close()
                f2.close()
                print(f"Data saved in file '{d}'.")
            else:
                print("Not saving data.")
                f.close()
        except OSError as e:
            print(f"Error opening file '{file}': {e}", file=sys.stderr)
    else:
        print("Usage : ft_ancient_text.py <file>")
