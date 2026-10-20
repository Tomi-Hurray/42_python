from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class representing a creature entity."""

    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.type = creature_type

    @abstractmethod
    def attack(self) -> str:
        """Execute the creature's attack and return a message."""
        pass

    def describe(self) -> str:
        """Return a standard description built from the name and type."""
        return f"{self.name} is a {self.type} type Creature"


class TransformCapability(ABC):
    """Mixin/Interface for creatures capable of transforming."""

    def __init__(self) -> None:
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        """Transform the creature into an altered state."""
        pass

    @abstractmethod
    def revert(self) -> str:
        """Revert the creature back to its normal state."""
        pass


class Flameling(Creature):
    """Base fire creature."""

    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    """Evolved fire/flying creature."""

    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Shiftling(Creature, TransformCapability):
    """Base transforming creature."""

    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} transforms into a boosted form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} reverts to its normal form."

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} attacks with transformed power!"
        return f"{self.name} attacks normally."


class Morphagon(Creature, TransformCapability):
    """Evolved transforming creature."""

    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} transforms into an apex dragon form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} reverts to its normal form."

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} unleashes a devastating transformed attack!"
        return f"{self.name} attacks normally."
