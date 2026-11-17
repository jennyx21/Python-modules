def secure_archive(name: str, mode: str = "",
                   cont: str = "") -> tuple[bool, str]:
    if mode == "w":
        try:
            with open(name, mode) as file:
                file.write(cont)
                return (True, "'content successfully written to file'")
        except (FileNotFoundError, PermissionError) as e:
            return (False, str(e))
    elif mode == "r":
        try:
            with open(name, mode) as file:
                c: str = file.read()
                return (True, c)
        except (FileNotFoundError, PermissionError) as e:
            return (False, str(e))
    else:
        return (False, "use 'r' for read or 'w' for write")


def main() -> None:
    print("=== Cyber Archives Security ===")
    print("\nusing 'secure_archive' to read from nonexisting file:")
    print(secure_archive("file_not_exitst", "r"))
    print("\nusing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("tast.txt", "r"))
    print("\nusing 'secure_archive' to read from a regular file:")
    print(secure_archive("test.txt", "r"))
    print("\nusing 'secure_archive' to read from a regular file:")
    print(secure_archive("test.txt", "w", "content"))


if __name__ == "__main__":
    main()
