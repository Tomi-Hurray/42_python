def garden_operations(operation_number: int) -> None:

    if (operation_number == 0):
        x: int = int("Hello World")
        print(x)
    elif (operation_number == 1):
        x: int = 10/0
    elif (operation_number == 2):
        x: int = open("text.tx", "r")
        x.close()
    elif (operation_number == 3):
        x: int = "Hello Wolrd" + 15
    elif (operation_number == 4):
        x: int = 69 + 67


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    i: int = 0
    while (i <= 4):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
        except ValueError as e:
            print(f"Caught ValueError error: {e}\n")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError error: {e}\n")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError error: {e}\n")
        except TypeError as e:
            print(f"Caught TypeError error: {e}\n")
        else:
            print("Operation completed successfully")
        i += 1

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
