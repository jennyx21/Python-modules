from .dark_validator import dark_validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    allowed = [
        "bats",
        "frogs",
        "arsenic",
        "eyball"
    ]
    return (allowed)


def dark_spell_record(spell_name: str, ingredients: str):
    print(f"{dark_validate_ingredients(ingredients)}")
