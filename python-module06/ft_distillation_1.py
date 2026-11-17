import alchemy
from alchemy import healing_potion as heal


def main():
    print("=== Distillation 1 ===")
    print("Using: 'import alchemy' structure to access potions")
    print(f"Testing strength_potion: {alchemy.strength_potion()}")
    print(f"Testing healing_potion: {heal()}")


if __name__ == "__main__":
    main()
