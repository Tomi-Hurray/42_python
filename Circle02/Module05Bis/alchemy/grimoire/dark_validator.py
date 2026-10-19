from alchemy.grimoire.dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    is_valid = any(
        ingredient.casefold() in ingredients.casefold()
        for ingredient in allowed
    )

    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients}: {status}"
