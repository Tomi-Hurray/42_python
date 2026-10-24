try:
    from datetime import datetime
    import enum
    from pydantic import BaseModel, Field, model_validator
except ImportError as e:
    print("Required modules are not installed. Please install "
          "pydantic and enum.")
    raise e


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
    def check_id_AC(self) -> "AlienContact":
        if not self.contact_id.startswith("AC-"):
            raise ValueError("contact_id must start with 'AC-'")
        else:
            return self

    @model_validator(mode="after")
    def validate_contact(self) -> "AlienContact":
        if self.contact_type == ContactType.PHYSICAL and \
           self.is_verified is False:
            raise ValueError("Physical contacts must be verified.")
        else:
            return self

    @model_validator(mode="after")
    def validate_telepathic_contact(self) -> "AlienContact":
        if self.contact_type == ContactType.TELEPATHIC and \
           self.witness_count < 3:
            raise ValueError("Telepathic contacts must have at least 3 "
                             "witnesses.")
        else:
            return self

    @model_validator(mode="after")
    def print_message_if_strong_signal(self) -> "AlienContact":
        if self.signal_strength > 7.0:
            pass  # Placeholder for any action, e.g., logging or printing
        else:
            raise ValueError("Signal strength must be greater than 7.0 for "
                             "this validation.")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 30)
    # Example usage of the AlienContact class
    contact = AlienContact(
        contact_id="AC-12345",
        timestamp=datetime.now(),
        location="Sector 7G",
        contact_type=ContactType.RADIO,
        signal_strength=7.5,
        duration_minutes=30,
        witness_count=4,
        message_received="We come in peace.",
        is_verified=True
    )

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

    try:
        invalid_contact = AlienContact(
            contact_id="12345",  # Does not start with 'AC-'
            timestamp=datetime.now(),
            location="A",  # Below min length
            contact_type=ContactType.PHYSICAL,
            signal_strength=15.0,  # Exceeds max value
            duration_minutes=-10,  # Below min value
            witness_count=0,  # Below min value
            message_received="This message is way too long." * 20,
            is_verified=False
        )
        print("Attempting to create an invalid contact...\n")
        print("Invalid contact report created (this should not happen):")
        print("ID:", invalid_contact.contact_id)
        print("Timestamp:", invalid_contact.timestamp)
        print("Location:", invalid_contact.location)
        print("Type:", invalid_contact.contact_type)
        print("Signal Strength:", invalid_contact.signal_strength)
        print("Duration:", invalid_contact.duration_minutes, "minutes")
        print("Witness Count:", invalid_contact.witness_count)
        print("Message Received:", invalid_contact.message_received)
        print("Verified:", "Yes" if invalid_contact.is_verified else "No")
    except Exception as e:
        print("Validation error:", e)


if __name__ == "__main__":
    main()
