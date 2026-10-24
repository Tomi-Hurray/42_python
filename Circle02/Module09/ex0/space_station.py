try:
    from datetime import datetime
    from pydantic import BaseModel, Field
except ImportError as e:
    print("Required modules are not installed. Please install pydantic.")
    raise e


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=1, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(gt=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    # Example usage of the SpaceStation class
    station = SpaceStation(
        station_id="ISS",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime.now(),
        is_operational=True,
        notes="All systems are functioning within normal parameters."
    )
    print("Valid station created:")
    print("ID:", station.station_id)
    print("Name:", station.name)
    print("Crew Size:", station.crew_size, "people")
    print("Power Level:", station.power_level, "%")
    print("Oxygen Level:", station.oxygen_level, "%")
    print("Status:", "Operational" if station.is_operational else
          "Not Operational")
    print("=" * 30)
    print("Attempting to create an invalid station...\n")

    try:
        invalid_station = SpaceStation(
            station_id="",
            name="A" * 51,  # Exceeds max length
            crew_size=0,  # Below min value
            power_level=150.0,  # Exceeds max value
            oxygen_level=-10.0,  # Below min value
            last_maintenance=datetime.now(),
            is_operational=True,
            notes="This note is way too long." * 20  # Exceeds max length
        )
        print("Invalid station created (this should not happen):")
        print("ID:", invalid_station.station_id)
        print("Name:", invalid_station.name)
        print("Crew Size:", invalid_station.crew_size, "people")
        print("Power Level:", invalid_station.power_level, "%")
        print("Oxygen Level:", invalid_station.oxygen_level, "%")
        print("Status:", "Operational" if invalid_station.is_operational else
              "Not Operational")
    except Exception as e:
        print("Validation error:", e)


if __name__ == "__main__":
    print("Space Station Data Validation")
    print("=" * 30)
    main()
