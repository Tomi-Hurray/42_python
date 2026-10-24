from enum import Enum
from pydantic import BaseModel, Field

class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length = 3, max_length = 10)
    name: str = Field(min_length = 2, max_length = 50)
    rank: Rank
    age: int = Field(ge = 18, le = 80)
    specialization: str = Field(min_length = 3, max_length = 30)
    years_experience: int = Field(ge = 0, le = 50)
    is_active: bool = Field(default = True)

class SpaceMission(BaseModel):
    mission_id: str = Field(min_length = 5, max_length = 15)
    mission_name: str = Field(min_length = 3, max_length = 100)
    destination: str = Field(min_length = 3, max_length = 50)
    launch_date: DateTime
    duration_days: int = Field(ge = 1, le 3650)
    crew: list[CrewMember] = Field(ge = 1, le =12)
    mission_status: str = Field(default = "planned")
    budget_millions: float = Field(ge = 1.0, le = 10000.0)

@model_validator
def mission_id_checker(self):
    