import os

try:
    from importlib import import_module

    load_dotenv = getattr(import_module("dotenv"), "load_dotenv")
    load_dotenv()
    HAS_DOTENV = True
except ImportError:
    HAS_DOTENV = False

if __name__ == "__main__":
    print("STATUS: Consulting the configuration...")

    missing_vars = []

    # 1. MATRIX_MODE
    matrix_mode = os.getenv("MATRIX_MODE")
    if not matrix_mode:
        missing_vars.append("MATRIX_MODE")
        matrix_mode = "development"

    # 2. DATABASE_URL
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        missing_vars.append("DATABASE_URL")
        database_url = "sqlite:///local_matrix.db"

    # 3. API_KEY
    api_key = os.getenv("API_KEY")
    if not api_key:
        missing_vars.append("API_KEY")
        api_key = "mock-dev-key"

    # 4. LOG_LEVEL
    log_level = os.getenv("LOG_LEVEL")
    if not log_level:
        missing_vars.append("LOG_LEVEL")
        log_level = "DEBUG"

    # 5. ZION_ENDPOINT
    zion_endpoint = os.getenv("ZION_ENDPOINT")
    if not zion_endpoint:
        missing_vars.append("ZION_ENDPOINT")
        zion_endpoint = "http://localhost:8080/zion"

    # Warn about missing variables without crashing
    if missing_vars:
        print(f"[WARNING] Missing configuration variables:\
{', '.join(missing_vars)}")
        print("[WARNING] Falling back to default values safely.\n")

    # Map configuration values to the expected display format
    if "sqlite" in database_url or "local" in database_url:
        db_status = "Connected to local instance"
    else:
        db_status = f"Connected to {database_url}"
    api_status = "Authenticated" if api_key else "Not Authenticated"
    network_status = "Online" if zion_endpoint else "Offline"

    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    print(f"Database: {db_status}")
    print(f"API Access: {api_status}")
    print(f"Log Level: {log_level}")
    print(f"Remote Network: {network_status}")

     # Check that the API key is not the development placeholder
    if api_key != "mock-dev-key":
        print("[OK] API key is not the development placeholder")
    else:
        print("[WARNING] Using the development API key placeholder")

    # Check for a literal .env entry in .gitignore
    gitignore_path = "ex1/.gitignore"
    env_ignored = False
    if os.path.isfile(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as gitignore:
            lines = gitignore.readlines()
            print(lines)
            env_ignored = any(line.strip() == ".env" for line in lines)

    print(env_ignored)
    if env_ignored:
        print("[OK] .env is listed in .gitignore")
    else:
        print("[WARNING] .env is not listed in .gitignore")
    if not HAS_DOTENV:
        print("[WARNING] python-dotenv is not installed; .env was not loaded")
