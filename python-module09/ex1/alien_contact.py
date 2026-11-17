from pydantic import BaseModel, Field, ValidationError, model_validator

from datetime import datetime
from enum import Enum
from typing import Optional


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATIC = "telepatic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minuts: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_receives: Optional[str] = Field(max_length=200)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def late_validation(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Invalid Id. ID must star with AC")
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact need to be verified")
        if (self.contact_type == ContactType.TELEPATIC
           and self.witness_count < 3):
            raise ValueError("Telepatic contact requires"
                             " at least 3 witnesses")
        if self.signal_strength > 7.0 and not self.message_receives:
            raise ValueError("this signal strengh should"
                             " include messages")
        return self

    def print_values(self) -> None:
        print("Alien Contact Log Validation")
        print(f"ID: {self.contact_id}")
        print(f"Type: {self.contact_type._value_}")
        print(f"Location: {self.location}")
        print(f"Signal: {self.signal_strength}/10")
        print(f"Duration: {self.duration_minuts} minutes")
        if self.message_receives is not None:
            print(f"Notes: {self.message_receives}")


def testing_valid_contact() -> None:
    contact = {
        "contact_id": "AC_2026_005",
        "timestamp": datetime(2026, 5, 2, 4, 49),
        "location": "Area 42, Heilbronn",
        "contact_type": ContactType.RADIO,
        "signal_strength": 4.2,
        "duration_minuts": 42,
        "witness_count": 5,
        "message_receives": "hallllllooooo frooom ZETA",
        "is_verified": False
    }
    try:
        stat = AlienContact.model_validate(contact)
        stat.print_values()
    except ValidationError as e:
        for er in e.errors():
            if er["type"] == "value_error":
                error = er["msg"].split(", ")
                print(f"{error[1]}")
            else:
                print(f"{er['msg']}")


def testing_invalid_contact() -> None:
    contact = {
        "contact_id": "AC_2026_005",
        "timestamp": datetime(2026, 5, 2, 4, 49),
        "location": "Area 42, Heilbronn",
        "contact_type": ContactType.TELEPATIC,
        "signal_strength": 4.2,
        "duration_minuts": 42,
        "witness_count": 2,
        "message_receives": "hallllllooooo frooom ZETA",
        "is_verified": False
    }
    try:
        stat = AlienContact.model_validate(contact)
        stat.print_values()
    except ValidationError as e:
        for er in e.errors():
            if er["type"] == "value_error":
                error = er["msg"].split(", ")
                print(f"{error[1]}")
            else:
                print(f"{er['msg']}")


def main() -> None:
    print("Alien Contact Log Validation")
    print("=========================================")
    testing_valid_contact()
    print()
    print("=========================================")
    print("Expected Validation error:")
    testing_invalid_contact()


if __name__ == "__main__":
    main()
