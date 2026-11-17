import alchemy.grimoire


def main():
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly ")
    print("Testing record light spell:", end="")
    print(f" {alchemy.grimoire.light_spell_record('Fantasy', 'earth wind')}")


if __name__ == "__main__":
    main()
