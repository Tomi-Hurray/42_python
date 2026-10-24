from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field, model_validator


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10_000.0)

    @model_validator(mode="after")
    def validate_mission(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("mission_id must start with 'M-'")

        inactive = [member.name for member in self.crew
                    if not member.is_active]
        if inactive:
            raise ValueError(f"Crew members must be active:\
                              {', '.join(inactive)}")

        if not any(
            member.rank in (Rank.CAPTAIN, Rank.COMMANDER)
            for member in self.crew
        ):
            raise ValueError(
                "There must be at least one captain or commander in the crew."
            )

        if self.duration_days > 365:
            rookies = sum(
                member.years_experience < 5 for member in self.crew
            )
            if rookies / len(self.crew) > 0.5:
                raise ValueError(
                    "At least 50% of the crew must have 5 or more years of "
                    "experience for missions longer than 1 year."
                )

        return self


def main() -> None:
    print("Space Mission Validation")
    print("=" * 30)
    # Example usage of the SpaceMission class
    crew_members = [
        CrewMember(
            member_id="CM-001",
            name="Alice Johnson",
            rank=Rank.CAPTAIN,
            age=35,
            specialization="Pilot",
            years_experience=4,
            is_active=True
        ),
        CrewMember(
            member_id="CM-002",
            name="Bob Smith",
            rank=Rank.OFFICER,
            age=28,
            specialization="Engineer",
            years_experience=4,
            is_active=True
        )
    ]

    mission = SpaceMission(
        mission_id="M-12345",
        mission_name="Lunar Exploration",
        destination="Moon",
        launch_date=datetime.now(),
        duration_days=180,
        crew=crew_members,
        mission_status="planned",
        budget_millions=500.0
    )
    print("Valid mission created:")
    print("ID:", mission.mission_id)
    print("Name:", mission.mission_name)
    print("Destination:", mission.destination)
    print("Launch Date:", mission.launch_date)
    print("Duration:", mission.duration_days, "days")
    print("Crew Size:", len(mission.crew))
    print("Status:", mission.mission_status)
    print("Budget:", mission.budget_millions, "million USD")
    print("Crew size:", len(mission.crew))
    print("Crew members:"
          f" {', '.join(member.name for member in mission.crew)}")
    print("=" * 30)

    try:
        invalid_mission = SpaceMission(
            mission_id="M12345",  # Invalid ID
            mission_name="A" * 10,  # Exceeds max length
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=400,  # Exceeds max duration for rookies
            crew=crew_members,
            mission_status="planned",
            budget_millions=500.0
        )
        print("Attempting to create an invalid mission...\n")
        print("Invalid mission created (this should not happen):")
        print("ID:", invalid_mission.mission_id)
        print("Name:", invalid_mission.mission_name)
        print("Destination:", invalid_mission.destination)
        print("Launch Date:", invalid_mission.launch_date)
        print("Duration:", invalid_mission.duration_days, "days")
        print("Crew Size:", len(invalid_mission.crew))
        print("Status:", invalid_mission.mission_status)
        print("Budget:", invalid_mission.budget_millions, "million USD")
    except Exception as e:
        print("Validation error:", e)


if __name__ == "__main__":
    main()
