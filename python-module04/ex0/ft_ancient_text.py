import sys
import typing


def ancient_text(file: typing.IO[str] | None) -> None:
    print(f"Accessing file '{sys.argv[1]}'")
    if file:
        content = file.read()
    print("---\n")
    print(f"{content}")
    print("\n---")


def main() -> None:
    print("=== Cyber Archives Recovery ===")
    if len(sys.argv) == 2:
        f = sys.argv[1]
        file = None
        try:
            file = open(f)
            ancient_text(file)
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{f}': {e}")
        finally:
            if file is not None:
                file.close()
                print(f"File '{f}' closed.")
    else:
        print("Usage: python3 ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
