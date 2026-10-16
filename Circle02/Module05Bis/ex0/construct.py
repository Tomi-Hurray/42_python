import os
import sys
import site


def check_virtual_env():
    is_venv = False

    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix')
                                       and sys.base_prefix != sys.prefix):
        is_venv = True
    elif 'VIRTUAL_ENV' in os.environ:
        is_venv = True

    elif 'CONDA_PREFIX' in os.environ:
        is_venv = True
    if is_venv is False:
        print("\nLABORATORY STATUS: You are working in the open\n")
        print(f"Current Python: {sys.version.split()[0]}")
        print("Virtual Environment: None detected")
        print("WARNING: You are in the global environment!\n"
              "Every reagent you install here leaks into the whole system.\n"
              "To seal the laboratory, run:\n"
              "python3 -m venv lab_env\n"
              "source lab_env/bin/activate # On Unix\n"
              "lab_env\\Scripts\\activate # On Windows\n"
              "\nThen run this program again.")
    else:
        print("\nLABORATORY STATUS: The laboratory is sealed\n")
        print(f"Current Python: {sys.version.split()[0]}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment path: {sys.executable}\n")

        print("SUCCESS: You are working in an isolated environment!\n"
              "Safe to install reagents without affecting\n"
              "the global system.\n")
        print("Reagent installation path:")
        print(site.getsitepackages())


if __name__ == "__main__":
    check_virtual_env()
