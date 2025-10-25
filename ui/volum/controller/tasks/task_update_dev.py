import concurrent.futures
import json
import os
import zipfile
from io import BytesIO
from pathlib import Path
from lxml.etree import XSLTApplyError
import threading

from volum.controller.tasks.taskbase import TaskBase
from volum.utils import utils_fb2txt
from volum.i18l.messages import *

threading.stack_size(128 * 2 ** 20)


class UpdateDev(TaskBase):

    def __init__(self):
        TaskBase.__init__(self)

    @staticmethod
    def update_dev(self) -> int:
        super()._check(self)
        return self._do(self)

    @staticmethod
    def _do(self) -> int:
        return self._do_update(self)

    @staticmethod
    def _get_inpx(self):
        folder_inpx = self.model.path_librusec + "/.."
        list_inpx = [
            (
                self.model.path_librusec + "/../" + inpx,
                os.path.getmtime(self.model.path_librusec + "/../" + inpx)
            )
            for inpx in os.listdir(folder_inpx)
            if inpx.endswith(".inpx")
        ]
        list_inpx.sort(key=lambda x: x[1])
        self.controller.log.info("Загрузка... | " + str(list_inpx[-1][0]).split("/")[-1])
        ref_json = dict()
        with zipfile.ZipFile(file=list_inpx[-1][0]) as f:
            with f.open("online.inp", mode="r") as file:
                inp = file.read()
                output_inpx = "online.inp"
                with open(output_inpx, mode="wb") as fw:
                    fw.write(inp)
                with open(output_inpx, mode="rb") as fr:
                    txt = fr.readlines()
                    for t in txt:
                        a = t.decode().strip().split("")
                        ref_json[a[5]] = a
        authors = set()
        genres = set()
        series = set()
        for book_id in ref_json:
            a = str(ref_json[book_id][0]).split(":")
            for item in a:
                if item.strip():
                    authors.add(item.strip())

            g = str(ref_json[book_id][1]).split(":")
            for item in g:
                if item.strip():
                    genres.add(item.strip())

            s = str(ref_json[book_id][3])
            if s.strip():
                series.add(s.strip())
        authors = list(authors)
        authors.sort()
        genres = list(genres)
        genres.sort()
        series = list(series)
        series.sort()
        with open(self.model.path_data + "/authors.json", mode="w", encoding="utf-8") as f:
            json.dump(authors, f)
        with open(self.model.path_data + "/genres.json", mode="w", encoding="utf-8") as f:
            json.dump(genres, f)
        with open(self.model.path_data + "/series.json", mode="w", encoding="utf-8") as f:
            json.dump(series, f)
        # with open(self.model.path_data + "/online.inp.json", mode="w", encoding="utf-8") as f:
        #     json.dump(ref_json, f)
        # with open(self.model.path_data + "/archives.json", mode="w", encoding="utf-8") as f:
        #     json.dump(archives, f)
        return ref_json

    @staticmethod
    def _do_update(self) -> int:
        ref_json = self._get_inpx(self)
        archives = [
            a for a in Path(self.model.path_librusec).iterdir() if a.suffix == ".zip"
        ]
        skip = 0
        if skip < 0:
            skip = 0
        self.controller.log.info(self.model.i18l.t(COUNT_SKIP_ARCHIVES_).format(skip))
        self.analyze = dict()
        for genre in self.model.allow_genres:
            self.analyze[genre] = 0
        index = 0
        results = []
        futures = dict()
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.model.max_workers) \
                as executor:
            for inner_archive in archives[skip:]:
                # self._analyze_size(self, inner_archive, ref_json)
                # continue
                vl_path = self.model.path_temp_vl + "VL" + inner_archive.name[3:-4] + ".fb2.zip"
                if os.path.exists(vl_path):
                    continue
                index += 1
                # self.worker(self, inner_archive, ref_json, index)
                futures[inner_archive] = \
                    executor.submit(self.worker, self, inner_archive, ref_json, index)
                if index >= self.model.max_workers:
                    index = 0
            executor.shutdown()
            for i in futures:
                results.append(futures[i].result())
        return 0

    @staticmethod
    def worker(self, inner_archive, ref_json, index):
        # self.controller.log.info(f"№{index} Старт...")
        self._read_zip(self, inner_archive, ref_json, index)
        self._create_volumlib(self, inner_archive, index)
        return 0

    def _create_zip(self, inner_archive) -> int:
        txt_folder = self.model.path_temp_txt + "txt-" + inner_archive + "/"
        zip_file_name = (
                self.model.path_data + "/txt/txt-" + inner_archive + ".zip"
        )
        if os.path.exists(zip_file_name):
            return 0
        txt_folder_list = [
            {"src": txt_folder + txt, "dsc": txt}
            for txt in os.listdir(txt_folder)
            if txt.endswith(".txt")
        ]
        if not txt_folder_list:
            return 0

        self.controller.log.info(f"Сжатие текста... | {zip_file_name}")
        zip_file = zipfile.ZipFile(
            file=zip_file_name,
            mode="w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
        )
        for item in txt_folder_list:
            zip_file.write(item["src"], item["dsc"])
        zip_file.close()
        return 0

    @staticmethod
    def _analyze_size(self, inner_archive, ref_json):
        fb2_path = self.model.path_temp_fb2 + "fb2" + inner_archive.name[3:-4]
        fb2_list = [name for name in os.listdir(fb2_path)]
        for fb2 in fb2_list:
            size = os.path.getsize(fb2_path + "/" + fb2)
            try:
                genres = ref_json[fb2[:-8]][1].split(":")
            except KeyError:
                continue
            for genre in genres:
                try:
                    g = genre.strip()
                    self.analyze[g] += size
                    self.controller.log.progress(
                        "Анализ размера... | "
                        + inner_archive.name + " | "
                        + fb2 + " | "
                        + g + " | "
                        + str(self.analyze[g] / 1024 / 1024).split(".")[0] + " MB"
                    )
                except KeyError:
                    continue

    def _create_volumlib(self, inner_archive, index):
        fb2_path = self.model.path_temp_fb2 + "fb2" + inner_archive.name[3:-4]
        parts = inner_archive.name[3:-4].split("-")
        new_filename = parts[0].rjust(7, "0") + "-" + parts[1].rjust(7, "0")
        vl_path = self.model.path_temp_vl + "VL-" + new_filename + ".fb2.zip"
        fb2_zips = [name for name in os.listdir(fb2_path)]
        temp_fb2 = self.model.path_temp_vl + "temp.fb2"
        zip_file = zipfile.ZipFile(
            file=vl_path,
            mode="w",
            compression=zipfile.ZIP_DEFLATED,
            compresslevel=9,
        )
        count = 0
        for fz in fb2_zips:
            with zipfile.ZipFile(file=fb2_path + "/" + fz) as f:
                with f.open(f.namelist()[0]) as file:
                    fb2 = file.read()
                with open(temp_fb2, mode="wb") as xml:
                    xml.write(fb2)
            if len(fb2) > 100 * 2 ** 10:
                zip_file.write(temp_fb2, fz[:-4])
                count += 1
                self.controller.log.progress(
                    "№" + str(index).rjust(4, "0") + " Создание архива...      | "
                    + " VL-" + new_filename + ".fb2.zip" + "  | "
                    + fz[:-4]

                )
            os.remove(temp_fb2)
        zip_file.close()
        if count == 0:
            os.remove(vl_path)
        print("")

    def _read_zip(self, inner_archive, ref_json, index) -> list:
        result = []
        language = "ru"
        archive = zipfile.ZipFile(inner_archive)
        txt_path = self.model.path_temp_txt + "txt" + inner_archive.name[3:-4]
        fb2_path = self.model.path_temp_fb2 + "fb2" + inner_archive.name[3:-4]
        allow_genres = self.model.allow_genres
        os.makedirs(fb2_path, exist_ok=True)
        os.makedirs(txt_path, exist_ok=True)
        name_list = archive.namelist()
        for name in name_list:
            if not name.endswith(".zip"):
                continue
            with archive.open(name) as inner_zip:
                fb2_zip = BytesIO(inner_zip.read())
                with zipfile.ZipFile(file=fb2_zip) as f:
                    with f.open(f.namelist()[0]) as file:
                        xml = file.read()
                        xml_name = f.namelist()[0][:-4] + ".xml"
                        only_name = f.namelist()[0][:-4]
                        xml_path = str(os.path.join(txt_path, xml_name).replace(
                            "\\",
                            "/",
                        ))
            if not os.path.exists(xml_path):
                with open(xml_path, mode="wb") as file_xml:
                    file_xml.write(xml)
            if not xml:
                self.controller.log.warn(f"XML-документ '{xml_name}' пустой")
                continue
            self.controller.log.progress(
                "№" + str(index).rjust(4, "0") + " Валидация/Обновление... | "
                + inner_archive.name
                + "   | "
                + language
                + " | .../"
                + "/".join(xml_path[:-4].split("/")[-4:])
            )
            try:
                text_exists = os.path.exists(xml_path[:-4] + ".txt")
                if not text_exists:
                    language, foreign = utils_fb2txt(xml_path, xml_path[:-4] + ".txt")
                text_exists = os.path.exists(xml_path[:-4] + ".txt")
                if os.path.exists(xml_path[:-4] + ".txt"):
                    with open(xml_path[:-4] + ".txt") as txt_file:
                        result.append(txt_file.read())
                fb2_file_name = fb2_path + "/" + name[:-4] + ".fb2"
                zip_file_name = fb2_file_name + ".zip"
                allow_genre = False
                genres = []
                try:
                    genres = str(ref_json[only_name][1]).split(":")
                except KeyError:
                    allow_genre = True
                for genre in genres:
                    g = genre.strip()
                    if g and (g in allow_genres):
                        allow_genre = True
                        break
                if not allow_genre and os.path.exists(zip_file_name):
                    os.remove(zip_file_name)
                if allow_genre and \
                        text_exists and \
                        os.path.exists(xml_path) and \
                        not os.path.exists(zip_file_name):
                    if not os.path.exists(fb2_file_name):
                        with open(fb2_file_name, mode="wb") as ffb2:
                            ffb2.write(xml)
                    zip_file = zipfile.ZipFile(
                        file=zip_file_name,
                        mode="w",
                        compression=zipfile.ZIP_DEFLATED,
                        compresslevel=9,
                    )
                    zip_file.write(fb2_file_name, name[:-4] + ".fb2")
                    zip_file.close()
                    os.remove(fb2_file_name)
            except XSLTApplyError as e:
                self.controller.log.warn(f"XSLTApplyError: {e}")
        archive.close()
        print("")
        return result
