from ex3 import TransformCreatureFactory, Creature, TransformCapability


def exercise_entity(label: str, entity: Creature) -> None:
    """Describe, attack, transform, attack again, and revert a transforming"""
    print(f"{label}:")
    print(entity.describe())
    print(entity.attack())

    if isinstance(entity, TransformCapability):
        print(entity.transform())
        print(entity.attack())
        print(entity.revert())


def main() -> None:
    print("Testing Creature with transform capability")
    factory = TransformCreatureFactory()

    base = factory.create_base()
    evolved = factory.create_evolved()

    exercise_entity("base", base)
    exercise_entity("evolved", evolved)


if __name__ == "__main__":
    main()
