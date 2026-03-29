def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return temp_int


def test_temperature(temp_str: str) -> None:
    print(f"Input data is:{temp_str}")
    try:
        x: int = input_temperature(temp_str)
        print(f"Temperature is now {x}")
    except ValueError:
        print(f"Caught input_temperature error: invalid literal for int()\
 with base 10: {temp_str}")


if __name__ == "__main__":
    test_temperature("25")
