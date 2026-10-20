from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Shiftling, Morphagon


class CreatureFactory(ABC):
    """Abstract factory for creating base and evolved creatures."""

    @abstractmethod
    def create_base(self) -> Creature:
        """Create and return the base form creature."""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Create and return the evolved form creature."""
        pass


class FlameFactory(CreatureFactory):
    """Factory for creating Fire-type creatures."""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    """Factory for creating Transforming creatures."""

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
