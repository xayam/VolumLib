from pyinstaller.client_volumlib import *

from volum.model.config import Config


def py_main() -> int:
    import PyInstaller.__main__

    PyInstaller.__main__.run(
        [
            "pyinstaller/client_volumlib.py",
            "--name=Portable-Client-VolumLib",
            "--distpath=dist",
            "--exclude-module=argostranslate",
            "--add-data=volum/*;volum/",
            "--add-data=pyinstaller/*;pyinstaller/",
            f"--icon={Config.ICON_ICO}",
            "--workpath=.",
            "--clean",
            "--onefile",
            "--windowed",
            "--noconsole",
        ],
    )
    return 0


if __name__ == "__main__":
    main()
    py_main()
