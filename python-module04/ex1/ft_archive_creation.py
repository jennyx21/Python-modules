import sys
import typing


def read_file(file: typing.IO[str] | None) -> str:
    print(f"Accessing file '{sys.argv[1]}'")
    if file:
        content: str = file.read()
    print("---\n")
    print(f"{content}")
    print("\n---")
    return content


def ft_transform_content(text: str) -> str:
    print("\nTransform data:")
    lines: list[str] = text.split("\n")
    lines = [line + "#" for line in lines]
    content = "\n".join(lines)
    print("---\n")
    print(f"{content}")
    print("\n---")
    return content


def main() -> None:
    print("=== Cyber Archives Recovery & Peservation ===")
    if len(sys.argv) == 2:
        f = sys.argv[1]
        file: typing.IO[str] | None = None
        try:
            file = open(f)
            text: str = read_file(file)
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error opening file '{f}': {e}")
        finally:
            if file is not None:
                file.close()
                print(f"File '{f}' closed.")
        transformed: str = ft_transform_content(text)
        name: str = str(input("Enter new file name (or empty):"))
        if not name:
            print("Not saving data.")
        else:
            print(f"Saving data to file '{name}")
            new_file: typing.IO[str] = open(name, "w")
            new_file.write(transformed)
            print(f"Data saved in file '{name}'.")
    else:
        print("Usage: python3 ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
