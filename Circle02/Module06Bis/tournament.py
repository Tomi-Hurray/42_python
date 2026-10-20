from typing import List, Tuple
from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory

from ex4 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    InvalidStrategyError,
)

Opponent = Tuple[CreatureFactory, BattleStrategy]


def format_opponents(opponents: List[Opponent]) -> str:
    """Build a readable summary string of the (Creature+Strategy) pairs."""
    parts = []
    for factory, strategy in opponents:
        creature_name = factory.create_base().name
        strat_name = strategy.__class__.__name__.replace("Strategy", "")
        parts.append(f"({creature_name}+{strat_name})")
    return f"[ {', '.join(parts)} ]"


def battle(opponents: List[Opponent]) -> None:
    """Pit every opponent against every other opponent once"""
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            entity1 = factory1.create_base()
            entity2 = factory2.create_base()

            print("- Battle *")
            print(entity1.describe())
            print("vs.")
            print(entity2.describe())
            print("now fight!")

            try:
                strategy1.act(entity1)
                strategy2.act(entity2)
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    normal_strategy = NormalStrategy()
    aggressive_strategy = AggressiveStrategy()

    # Tournament 0: Valid combinations
    t0_opponents: List[Opponent] = [
        (flame_factory, normal_strategy),
        (transform_factory, aggressive_strategy),
    ]
    print("Tournament 0 (basic)")
    print(format_opponents(t0_opponents))
    battle(t0_opponents)

    # Tournament 1: Invalid combination (Flameling with AggressiveStrategy)
    t1_opponents: List[Opponent] = [
        (transform_factory, aggressive_strategy),
        (flame_factory, aggressive_strategy),
    ]
    print("Tournament 1 (error)")
    print(format_opponents(t1_opponents))
    battle(t1_opponents)


if __name__ == "__main__":
    main()
