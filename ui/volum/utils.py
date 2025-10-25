import os
import re
import sys
from typing import Tuple
import pymorphy3
import chardet
import lxml.etree as etree
from langid import classify as detect_language
from stop_words import get_stop_words

from volum.model.fb2txt import FB2TXT

stop_words = get_stop_words("ru") + get_stop_words("en")
morph = pymorphy3.MorphAnalyzer()


def utils_fb2txt(input_fb2: str, output_txt: str) -> Tuple[str, int]:
    with open(input_fb2, mode="rb") as file:
        fb2 = file.read()
    root = etree.fromstring(text=fb2, parser=etree.XMLParser(recover=True))
    transform = FB2TXT
    transform = etree.fromstring(transform)
    txt = str(etree.XSLT(transform)(root))
    txt = re.compile(r"(\n\r)+").sub("\n", txt)
    txt = re.compile(r"\n+").sub("\n\n", txt)
    txt = txt.replace(" ", " ").strip()
    language = detect_language(txt)[0]
    if language != "ru":
        return language, 1
    with open(
            file=output_txt, mode="w", encoding="windows-1251", errors="replace", newline=""
    ) as file:
        file.write(txt)
    return language, 0


def utils_int44_to_bytes(key1: int, key2: int) -> bytes:
    key1 = ((2 ** 32 - 1) & key1) << (4 * 8)
    result = key1 | key2
    # print(result)
    result = result.to_bytes(length=8, byteorder=sys.byteorder)
    return result


def utils_split(text: str) -> dict:
    symbols_ru = r"ёйцукенгшщзхъфывапролджэячсмитьбю"
    symbols_en = r"qwertyuiopasdfghjklzxcvbnm"
    digits = r"1234567890"
    symbols = symbols_ru + symbols_en + digits
    result = [
        (str(morph.parse(text[m.start(): m.end()])[0].normal_form).lower(), m.start())
        for m in re.finditer("[{}]+".format(symbols), text, flags=re.IGNORECASE)
        if text[m.start(): m.end()].lower() not in stop_words
        if 1 < len(text[m.start(): m.end()]) < 20
    ]
    s = dict()
    for r in result:
        s.setdefault(r[0], []).append(r[1])
    return s


def utils_split_predlo(text: str) -> list:
    pattern = "[^\n]+"
    result = re.findall(pattern, text)
    # print(result)
    # sys.exit()
    if result:
        return result
    else:
        return []


def utils_delete_pyc(folder: str) -> None:
    pycs = os.listdir(folder)
    pycs = [pyc for pyc in pycs if pyc.endswith(".pyc")]
    for pyc in pycs:
        os.remove(folder + pyc)
    os.removedirs(folder)


def utils_detect_language(file_path: str) -> str:
    with open(file_path, "rb") as file:
        detector = chardet.universaldetector.UniversalDetector()
        for line in file:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    return detector.result["language"]


def utils_text_size(config, logger) -> None:
    files = []
    for folder in os.listdir(config.path_temp_txt):
        for file in os.listdir(config.path_temp_txt + folder):
            if folder.startswith("txt-") and file.endswith(".txt"):
                files.append(f"{config.path_temp_txt}{folder}/{file}")
                logger.progress(
                    f"Загружаю список текстовых файлов... | {folder}/{file}",
                    is_savelable=False,
                )
    logger.info(is_savelable=False)
    text_size = 0
    text_count = len(files)
    for index in range(text_count):
        text_size += os.stat(files[index]).st_size
        logger.progress(
            f"{str(index + 1).rjust(6, '0')}/{text_count} | "
            + f"Общий размер {str(text_size / 1024 ** 3).split('.')[0]}ГБ | "
            + str(files[index]).replace("\\", "/"),
            is_savelable=False,
        )
    logger.info(is_savelable=False)


if __name__ == "__main__":
    utils_int44_to_bytes(2, 2)
