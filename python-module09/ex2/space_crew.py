from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum
from typing import Annotated


class CrewRanks(Enum):
    CADET = "cadet"
    OFFiCER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    Name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_activ: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: Annotated[list[CrewMember], Field(min_length=1, max_length=12)]
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def late_validation(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Invalid Id. ID must star with: M")
        count = 0
        activ = 0
        experienced = 0
        total = 0
        for member in self.crew:
            if (member.rank == CrewRanks.COMMANDER
               or member.rank == CrewRanks.CAPTAIN):
                count += 1
            if member.is_activ:
                activ += 1
            if member.years_experience >= 5:
                experienced += 1
            total += 1
        if count < 1:
            raise ValueError("Mission must have at"
                             " least one Commander or Captain")
        if self.duration_days > 365 and experienced / total < 0.5:
            raise ValueError("For this duration at least 50%% of the members"
                             " need to have 5+ years of experience")
        if activ < total:
            raise ValueError("All crew members must be active")
        return self

    def print_svalues(self) -> None:
        print("Valid mission created:")
        print(f"Mission: {self.mission_name}")
        print(f"ID: {self.mission_id}")
        print(f"Destination: {self.destination}")
        print(f"Duration: {self.duration_days} days")
        print(f"Budget: ${self.budget_millions}M")
        print(f"Crew size: {self.crew.__len__()}")
        for memb in self.crew:
            print(f"- {memb.Name} ({memb.rank._value_}) -"
                  f" {memb.specialization}")


def testing_valid_misson() -> None:
    crew1 = {
        "member_id": "ID_0001",
        "Name": "Sarah Conner",
        "rank": CrewRanks.COMMANDER,
        "age": 30,
        "specialization": "Mission Command",
        "years_experience": 10,
        "is_activ": True
    }
    crew2 = {
        "member_id": "ID_0002",
        "Name": "John Smith",
        "rank": CrewRanks.LIEUTENANT,
        "age": 35,
        "specialization": "Navigation",
        "years_experience": 15,
        "is_activ": True
    }
    crew3 = {
        "member_id": "ID_0003",
        "Name": "Alice Johnson",
        "rank": CrewRanks.OFFiCER,
        "age": 24,
        "specialization": "Engineering",
        "years_experience": 4,
        "is_activ": True
    }
    crew_list = [
        CrewMember.model_validate(crew1),
        CrewMember.model_validate(crew2),
        CrewMember.model_validate(crew3)
    ]

    mission = {
        "mission_id": "M_2026_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": datetime(2026, 5, 2, 21, 58),
        "duration_days": 900,
        "crew": crew_list,
        "mission_status": "Ongoing",
        "budget_millions": 2500.0
    }
    try:
        stat = SpaceMission.model_validate(mission)
        stat.print_svalues()
    except ValidationError as e:
        for er in e.errors():
            if er["type"] == "value_error":
                error = er["msg"].split(", ")
                print(f"{error[1]}")
            else:
                print(f"{er['msg']}")


def testing_invalid_mission() -> None:
    crew1 = {
        "member_id": "ID_0001",
        "Name": "Sarah Conner",
        "rank": CrewRanks.CADET,
        "age": 30,
        "specialization": "Mission Command",
        "years_experience": 10,
        "is_activ": True
    }
    crew2 = {
        "member_id": "ID_0002",
        "Name": "John Smith",
        "rank": CrewRanks.LIEUTENANT,
        "age": 35,
        "specialization": "Navigation",
        "years_experience": 15,
        "is_activ": True
    }
    crew3 = {
        "member_id": "ID_0003",
        "Name": "Alice Johnson",
        "rank": CrewRanks.OFFiCER,
        "age": 24,
        "specialization": "Engineering",
        "years_experience": 4,
        "is_activ": True
    }
    crew_list = [
        CrewMember.model_validate(crew1),
        CrewMember.model_validate(crew2),
        CrewMember.model_validate(crew3)
    ]

    mission = {
        "mission_id": "M_2026_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": datetime(2026, 5, 2, 21, 58),
        "duration_days": 900,
        "crew": crew_list,
        "mission_status": "Ongoing",
        "budget_millions": 2500.0
    }
    try:
        stat = SpaceMission.model_validate(mission)
        stat.print_svalues
    except ValidationError as e:
        for er in e.errors():
            if er["type"] == "value_error":
                error = er["msg"].split(", ")
                print(f"{error[1]}")
            else:
                print(f"{er['msg']}")


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")
    testing_valid_misson()
    print()
    print("=========================================")
    print("Expected Validation error:")
    testing_invalid_mission()


if __name__ == "__main__":
    main()
