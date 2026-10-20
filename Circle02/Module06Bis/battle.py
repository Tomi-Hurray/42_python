from ex3 import CreatureFactory, FlameFactory, TransformCreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    """Create base and evolved entities from a factory."""
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def test_battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    """Pit the base entities of two factories against each other."""
    print("Testing battle")
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print("fight!")
    print(creature1.attack())
    print(creature2.attack())


def main() -> None:
    flame_factory = FlameFactory()
    transform_factory = TransformCreatureFactory()

    test_factory(flame_factory)
    test_factory(transform_factory)
    test_battle(flame_factory, transform_factory)


if __name__ == "__main__":
    main()
