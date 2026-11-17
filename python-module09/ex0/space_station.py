from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class Station(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(max_length=200)

    def print_svalues(self) -> None:
        print("valid station created")
        print(f"ID: {self.station_id}")
        print(f"Name: {self.name}")
        print(f"Crew: {self.crew_size} people")
        print(f"Power: {self.power_level}%")
        print(f"Oxygen: {self.oxygen_level}%")
        print(f"Maitanence: {self.last_maintenance}")
        if self.is_operational:
            print("Status: operational")
        else:
            print("Status: not operational")
        if self.notes is not None:
            print(f"Notes: {self.notes}")


def testing_valid_station() -> None:
    station = {
        "station_id": "SS123445",
        "name": "station1",
        "crew_size": 5,
        "power_level": 100.0,
        "oxygen_level": 80.5,
        "last_maintenance": datetime(2026, 5, 2, 3, 34),
        "is_operational": True,
        "notes": None
    }
    try:
        stat = Station.model_validate(station)
        stat.print_svalues()
    except ValidationError as e:
        for er in e.errors():
            print(er["msg"])


def testing_invalid_station() -> None:
    station = {
            "station_id": "SS123445",
            "name": "station1",
            "crew_size": 25,
            "power_level": 100.0,
            "oxygen_level": 80.5,
            "last_maintenance": datetime(2026, 5, 2, 3, 34),
            "is_operational": False,
            "notes": "hallo"
    }

    try:
        stat = Station.model_validate(station)
        stat.print_svalues
    except ValidationError as e:
        for er in e.errors():
            print(er["msg"])


def main() -> None:
    print("Space Station Data Validation")
    print("=========================================")
    testing_valid_station()
    print()
    print("=========================================")
    print("Expected Validation error:")
    testing_invalid_station()


if __name__ == "__main__":
    main()
