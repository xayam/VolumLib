import os
import shutil
import zipfile
from datetime import datetime

from app import App
from volum.model.query import Query
from volum import VERSION
from volum.entity import *
from pyinstaller.pyinstaller import main as _py_main


class Build:
    def __init__(self, release: bool = False, jobs=None):
        self.release = release
        self.jobs = jobs

    def run(self) -> int:
        result = 0
        result += self._prepare()
        if self.release:
            result += _py_main()
            result += self._complete()
            result += self._clear()
            result += self._zipped()
        return result

    @staticmethod
    def _zipped() -> int:
        zip_name = f"VolumLib-v{VERSION}.zip"
        zip_path = f"{TORRENTPATH}/{zip_name}"
        release = zipfile.ZipFile(
            zip_path, mode="w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
        )
        client = f"{CLIENTNAME}.exe"
        release.write(f"dist/{client}", client)
        # server = f"{SERVERNAME}.exe"
        # release.write(f"dist/{server}", server)
        # release.write("server.json", "server.json")
        # release.write("run-server.bat", "run-server.bat")
        release.write(
            "volum/model/resources",
            "volum/model/resources",
        )
        release.write("client.json", "client.json")
        release.write("run-client.bat", "run-client.bat")
        release.write(f"../README.md", "README.md")
        release.write(f"../LICENSE", "LICENSE")
        release.close()

        shutil.copyfile(zip_path, f"{TORRENTPATH}/{zip_name}")
        shutil.copyfile("data/__init__.py", f"{TORRENTPATH}/data/__init__.py")
        shutil.copyfile("data/index/wid.pkl", f"{TORRENTPATH}/data/index/wid.pkl")
        shutil.copytree(
            "data/index/zip",
            f"{TORRENTPATH}/data/index/zip",
            dirs_exist_ok=True,
        )
        shutil.copytree(
            "data/txt",
            f"{TORRENTPATH}/data/txt",
            dirs_exist_ok=True,
        )
        shutil.copyfile(
            "data/index/lmdb/__init__.py",
            f"{TORRENTPATH}/data/index/lmdb/__init__.py",
        )
        return 0

    @staticmethod
    def _clear() -> int:
        now = datetime.now()
        year = str(now.year)
        month = str(now.month).rjust(2, "0")
        day = str(now.day).rjust(2, "0")
        zip_release_list = [
            [f"{TORRENTPATH}/{i}", f"../../copy/{year}_{month}_{day}_{i}"]
            for i in os.listdir(TORRENTPATH)
            if i.endswith(".zip")
        ]
        for path in zip_release_list:
            os.replace(path[0], path[1])
        return 0

    def _prepare(self) -> int:
        if self.jobs is None:
            self.jobs = [
                TASK_TRANSLATE_DEV,
                TASK_UPDATE_DEV,
                # TASK_CREATE_DEV,
                TASK_BENCHMARKS,
            ]
        application = App(
            Query(
                jobs=self.jobs,
                target=TARGET_DEV,
                language=LANG_PRIMARY,
            )
        )
        return application.run()

    def _complete(self) -> int:
        application = App(
            Query(
                release=self.release,
                jobs=[],
                target=TARGET_CLIENT,
                language=LANG_PRIMARY,
            )
        )
        return application.run()


def main(release: bool = False, jobs=None) -> int:
    try:
        builder = Build(release=release, jobs=jobs)
        return builder.run()
    except Exception as e:
        print(f"{type(e)}: {e}")
        return 1


if __name__ == "__main__":
    main(release=True)
