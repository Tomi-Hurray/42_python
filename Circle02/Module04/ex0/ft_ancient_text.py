import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file = sys.argv[1]
        try:
            f = open(file)
            print(f"Error opening file: {file}")
            print("=== Cyber Archives Recovery & Preservation ======")
            print(f"Accessing file {file}")
            print("- - -\n")
            print(f.read())
            print("\n- - -")
            f.close()
            print("File 'ancient_fragment.txt' closed.")
        except OSError as e:
            print(f"Error opening file '{file}': {e}")
    else:
        print("Usage : ft_ancient_text.py <file>")
