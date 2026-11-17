from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    ingred = ingredients.split(" ")
    for i in ingred:
        if i in light_spell_allowed_ingredients():
            return (f"{', '.join(ingred)} VALID")
    return (f"{', '.join(ingred)} INVALID")
