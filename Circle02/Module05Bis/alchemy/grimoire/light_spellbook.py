from alchemy.grimoire.light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    status = result.rsplit(": ", 1)[-1]

    if status == "VALID":
        return f"{spell_name} recorded: {result}"
    return f"{spell_name} rejected: {result}"
