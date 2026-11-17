from .dark_spellbook import dark_spell_allowed_ingredients


def dark_validate_ingredients(ingredients: str):
    ingred = ingredients.split(" ")
    for i in ingred:
        if i in dark_spell_allowed_ingredients():
            return (f"{', '.join(ingred)} VALID")
    return (f"{', '.join(ingred)} INVALID")
