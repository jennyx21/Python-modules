
def main():
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly ")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    try:
        import alchemy.grimoire.dark_spellbook as dark
        print(f"{dark('Fantasy', 'frogs')}")
    except ImportError as e:
        print(f"this is the Error: {e}")


if __name__ == "__main__":
    main()
