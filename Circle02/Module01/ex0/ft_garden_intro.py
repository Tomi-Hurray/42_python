
def garden_info(name: str, height: float, age: int) -> None:
    print("=== Welcome to My Garden! ===")
    print(f"Plant:  {name}")
    print(f"Height: {height} cm")
    print(f"Age: {age} days")
    print("=== End of Program ===")


if __name__ == "__main__":
    garden_info("Kaktus", 5.55, 26)
