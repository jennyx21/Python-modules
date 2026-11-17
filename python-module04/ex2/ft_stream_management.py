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
            sys.stderr.write(f"[STDERR] Error opening file {f}: {e}")
            sys.stdout.flush()
        finally:
            if file is not None:
                file.close()
                print(f"File '{f}' closed.")
        transformed: str = ft_transform_content(text)
        sys.stdout.write("Enter new file name (or empty):")
        sys.stdout.flush()
        name: str = sys.stdin.readline().strip()
        if not name:
            print("Not saving data.")
        else:
            try:
                new_file: typing.IO[str] = open(name, "w")
                print(f"Saving data to file '{name}'")
                new_file.write(transformed)
                print(f"Data saved in file '{name}'.")
            except PermissionError as e:
                sys.stderr.write(f"[STDERR] Error opening file {name}: {e}\n")
                sys.stdout.flush()
                print("Data not saved.")

    else:
        print("Usage: python3 ft_ancient_text.py <file>")


if __name__ == "__main__":
    main()
