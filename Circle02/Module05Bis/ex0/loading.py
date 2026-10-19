from importlib.metadata import version
from importlib.metadata import PackageNotFoundError


def check_pandas() -> bool:
    try:
        version('pandas')
        return True
    except ModuleNotFoundError:
        return False


def check_numpy() -> bool:
    try:
        version("numpy")
        return True
    except PackageNotFoundError:
        return False


if __name__ == "__main__":
    print("REAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:\n")
    if check_pandas():
        print(f"[OK] pandas ({version('pandas')}) - Data manipulation ready")
    else:
        print("[TIP] pip install pandas")

    if check_numpy():
        print(f"[OK] numpy ({version('numpy')}) -  Numerical \
computation ready\n")
    else:
        print("[TIP] pip install numpy\n")

    print("pip vs Poetry:\n\
requirements.txt declares what to install; pip resolves it at install time.\n\
pyproject.toml declares the same constraints, and Poetry pins the resolved\n\
versions in poetry.lock so every install is identical.\n")

    if check_numpy() and check_pandas():
        print("All reagents present and accounted for.")
    else:
        print("Install all the reagents!")
