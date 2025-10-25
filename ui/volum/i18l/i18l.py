import importlib

from volum.const import *
from volum.entity import *


class I18L:
    PATH_LANG = PATH_LANG
    LANG_PRIMARY: str = LANG_PRIMARY
    LANG_SECONDARY: list = LANG_SECONDARY

    def __init__(self, language: str = LANG_PRIMARY):
        self.language = None
        self._messages = None
        self._standart = const_get_standart()

        self.set_language(language)

    def set_language(self, language: str = RUS) -> None:
        if self.language is None or self.language != language:
            try:
                self.language = language
                self._messages = getattr(importlib.import_module(
                    self.PATH_LANG + self.language
                ), MESSAGES)
            except ModuleNotFoundError:
                self.language = self.LANG_PRIMARY
                self._messages = getattr(importlib.import_module(
                    self.PATH_LANG + self.language
                ), MESSAGES)

    def t(self, key_message: str) -> str:
        return self._messages[key_message]

    def translate(self, path_lang: str = PATH_LANG) -> None:
        self.PATH_LANG = path_lang
        current_language = self.language
        self.set_language(language=self.LANG_PRIMARY)
        for to_code in self.LANG_SECONDARY:
            result = ""
            try:
                from volum.i18l.i18l_translate import Translate

                translater = Translate(from_code=self.language, to_code=to_code)
                for key_messages in self._messages:
                    text = translater.translate(text=self._messages[key_messages])
                    result += " " * 8 + f'{key_messages.upper()}: u"' + \
                              text.encode(errors='replace').decode(errors='ignore') + '", \n'
                i18l_lang = \
                    "from volum.const import *\n" + \
                    "from volum.i18l.messages import *\n\n\n" + \
                    "MESSAGES: dict = {}\n\n" + \
                    "const_assert_list(const_key_dict_to_list(MESSAGES))\n"
                with open(self.PATH_LANG.replace(".", "/") + to_code + ".py",
                          mode="w", encoding="utf-8") as f:
                    f.write(i18l_lang.format("{\n" + result + "    }\n"))
            except ModuleNotFoundError:
                pass
        self._test_languages()
        self.set_language(language=current_language)

    def _test_languages(self) -> None:
        for lang in self.LANG_SECONDARY:
            self.set_language(lang)


def main(path_lang=PATH_LANG):
    I18L().translate(path_lang=path_lang)


if __name__ == "__main__":
    main(path_lang="i18l_")
