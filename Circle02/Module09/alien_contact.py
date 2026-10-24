from datetime import datetime
import enum
from pydantic import BaseModel, Field, model_validator


class ContactType(str, enum.Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(gt=0, le=1440)
    witness_count: int = Field(gt=0, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def check_id_AC(self):
        if not self.contact_id.startswith("AC-"):
            raise ValueError("contact_id must start with 'AC-'")
        else:
            return self

    @model_validator(mode="after")
    def validate_contact(self):
        if self.contact_type == ContactType.PHYSICAL and \
           self.is_verified is False:
            raise ValueError("Physical contacts must be verified.")
        else:
            return self

    @model_validator(mode="after")
    def validate_telepathic_contact(self):
        if self.contact_type == ContactType.TELEPATHIC and \
           self.witness_count < 3:
            raise ValueError("Telepathic contacts must have at least 3 "
                             "witnesses.")
        else:
            return self

    @model_validator(mode="after")
    def print_message_if_strong_signal(self):
        if self.signal_strength > 7.0:
            print(self.message_received)
        else:
            return self


def main():
    print("Alien Contact Log Validation")
    print("=" * 30)
    # Example usage of the AlienContact class
    contact = AlienContact(
        contact_id="As-12345",
        timestamp=datetime.now(),
        location="Sector 7G",
        contact_type=ContactType.RADIO,
        signal_strength=5.5,
        duration_minutes=30,
        witness_count=2,
        message_received="We come in peace.",
        is_verified=True
    )
    try:
        AlienContact(**contact)
    except Exception as e:
        print("Validation error:", e)

    print("Valid contact report:")
    print("ID:", contact.contact_id)
    print("Timestamp:", contact.timestamp)
    print("Location:", contact.location)
    print("Type:", contact.contact_type)
    print("Signal Strength:", contact.signal_strength)
    print("Duration:", contact.duration_minutes, "minutes")
    print("Witness Count:", contact.witness_count)
    print("Message Received:", contact.message_received)
    print("Verified:", "Yes" if contact.is_verified else "No")
    print("=" * 30)
    print("Attempting to create an invalid contact...\n")

    invalid_contact = {
        "contact_id": "12345",  # Does not start with 'AC-'
        "timestamp": "2024-01-01T00:00:00",
        "location": "A",  # Below min length
        "contact_type": ContactType.PHYSICAL,
        "signal_strength": 15.0,  # Exceeds max value
        "duration_minutes": -10,  # Below min value
        "witness_count": 0,  # Below min value
        "message_received": "This message is way too long." * 20,
        "is_verified": False
    }
    try:
        AlienContact(**invalid_contact)
    except Exception as e:
        print("Validation error:", e)


if __name__ == "__main__":
    main()
