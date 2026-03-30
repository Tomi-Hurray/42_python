def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    return temp_int


def test_temperature(temp_str: str) -> None:
    print(f"Input data is:{temp_str}")
    try:
        x: int = input_temperature(temp_str)
        if x > 40:
            raise ValueError(f"{x}°C is too hot for plants (max 40°C)")
        if x < 0:
            raise ValueError(f"{x}°C is too cold for plants (min 0°C)")
        print(f"Temperature of {x}°C is good for plants!\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature("25")
    test_temperature("-32")
    test_temperature("abc")
    print("All test complete - program didn't crash!")
