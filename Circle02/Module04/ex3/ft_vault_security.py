def secure_archive(fname: str, mark=None, save=None) -> tuple[bool, str]:
    if mark != "write":
        mark = "read"
    if not save:
        save = "Hello World!"
    try:
        if mark == "read":
            with open(fname, "r") as f:
                content = f.read()
                return (True, content)
        else:
            with open(fname, "w") as f:
                f.write(save)
                msg = "Content successfully written to file"
                return (True, msg)
    except PermissionError as x:
        error = (f"Using 'secure_archive' to read from"
                 f" an inaccessible file: {x}")
        return (False, error)
    except OSError as e:
        error = (f"Using 'secure_archive' to read from"
                 f" a nonexistent file: {e}")
        return (False, error)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")
    fname = "ancient_fragment.txt"
    print(secure_archive(fname, "write"))
