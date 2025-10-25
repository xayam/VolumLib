from pyinstaller.pyinstaller_server_volumlib import py_main as py_server_main
from pyinstaller.pyinstaller_client_volumlib import py_main as py_client_main


def main() -> int:
    py_server_main()
    py_client_main()
    return 0


if __name__ == "__main__":
    main()
