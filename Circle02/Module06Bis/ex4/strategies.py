from abc import ABC, abstractmethod
from ex3.creatures import Creature, TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    """Abstract base class for creature battle strategies."""

    @abstractmethod
    def is_valid(self, entity: Creature) -> bool:
        """Return True if the entity is suitable for this strategy."""
        pass

    @abstractmethod
    def act(self, entity: Creature) -> None:
        """Execute the strategy actions with the given entity."""
        pass


class NormalStrategy(BattleStrategy):
    """Standard strategy suitable for any Creature."""

    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, Creature)

    def act(self, entity: Creature) -> None:
        if not self.is_valid(entity):
            name = getattr(entity, "name", str(entity))
            raise InvalidStrategyError(
                f"Invalid Creature '{name}' for this normal strategy"
            )
        print(entity.attack())


class AggressiveStrategy(BattleStrategy):
    """Aggressive strategy requiring TransformCapability."""

    def is_valid(self, entity: Creature) -> bool:
        return isinstance(entity, Creature) and isinstance(entity,
                                                           TransformCapability)

    def act(self, entity: Creature) -> None:
        if not self.is_valid(entity):
            name = getattr(entity, "name", str(entity))
            raise InvalidStrategyError(
                f"Invalid Creature '{name}' for this aggressive strategy"
            )
        # Type narrowing for static type checkers
        assert isinstance(entity, TransformCapability)
        print(entity.transform())
        print(entity.attack())
        print(entity.revert())
