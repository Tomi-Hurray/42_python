from alchemy.grimoire.dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = dark_validate_ingredients(ingredients)
    status = result.rsplit(": ", 1)[-1]

    if status == "VALID":
        return f"{spell_name} recorded: {result}"
    return f"{spell_name} rejected: {result}"
