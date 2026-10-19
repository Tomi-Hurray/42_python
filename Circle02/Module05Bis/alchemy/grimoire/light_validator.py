def validate_ingredients(ingredients: str) -> str:
    from alchemy.grimoire.light_spellbook import \
        light_spell_allowed_ingredients

    allowed = light_spell_allowed_ingredients()
    is_valid = any(
        ingredient.casefold() in ingredients.casefold()
        for ingredient in allowed
    )

    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients}: {status}"
