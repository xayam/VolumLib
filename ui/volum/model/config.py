import json
import sys

from volum import *


class Config:
    ###########################################################################
    # !!! CHANGE THIS PATHS FOR OWN DEVELOPMENT BUILDS !!!
    ###########################################################################
    path_librusec = "E:/Torrents/BigTorrent/Libruks/Архивы Либрусек"
    path_temp = "E:/Torrents/BigProgram/libruks/temp"  # auxiliary folder
    ###########################################################################

    path_temp_txt = path_temp + "/txt/"
    path_temp_fb2 = path_temp + "/fb2/"
    path_temp_vl = "E:/Torrents/MyTorrent/volumlib/VolumLib/volumlib/"
    max_workers = 999
    ICON_ICO = "volum/model/resources/logo.ico"
    ICON_PNG = "volum/model/resources/logo.png"
    app_version = VERSION
    app_name = "VolumLib"
    app_title = (
        "Библиотека полнотекстового поиска по архивам текстовых файлов Либрусека"
    )

    path_data = "data"
    path_log = "log.txt"
    savelable_log = 0

    allow_genres = ["child_sf", "comp_all", "comp_db", "comp_hard", "comp_osnet", "comp_programming",
                    "comp_soft", "comp_www", "epic", "fanfiction", "mystery", "popadanec",
                    "russian_fantasy", "sci_abstract", "sci_all", "sci_anachem",
                    "sci_biochem", "sci_biology", "sci_biophys", "sci_botany", "sci_build", "sci_business", "sci_chem",
                    "sci_cosmos", "sci_crib", "sci_culture", "sci_ecology", "sci_economy", "sci_geo",
                    "sci_juris", "sci_linguistic", "sci_math", "sci_medicine", "sci_medicine_alternative", "sci_metal",
                    "sci_orgchem", "sci_oriental", "sci_pedagogy", "sci_philology", "sci_philosophy", "sci_phys",
                    "sci_physchem", "sci_politics", "sci_popular", "sci_psychology", "sci_radio", "sci_religion",
                    "sci_social_studies", "sci_state", "sci_tech", "sci_textbook", "sci_theories", "sci_transport",
                    "sci_veterinary", "sci_zoo", "sf_action", "sf_all", "sf_cyberpunk", "sf_detective",
                    "sf_epic", "sf_etc", "sf_fantasy", "sf_fantasy_city", "sf_fantasy_irony", "sf_heroic",
                    "sf_humor", "sf_irony", "sf_litrpg", "sf_mystic", "sf_postapocalyptic",
                    "sf_space", "sf_space_opera", "sf_stimpank", "sf_technofantasy", "tech_all"]

    path_client_json = "client.json"
    path_server_json = "server.json"

    controller = None
    path_json: str = None

    theme_style = "Dark"
    BG_STYLE_NORMAL = {
        "Dark": "volum/model/resources/black.png",
        "Light": "volum/model/resources/white.png",
    }
    BG_STYLE_DOWN = {
        "Dark": "volum/model/resources/blue.png",
        "Light": "volum/model/resources/blue.png",
    }

    def __init__(self):
        pass

    def app_header(self):
        return f"{self.app_name} v{self.app_version}"

    def load_options(self) -> int:
        try:
            self.path_json = sys.argv[1]
            result = self._load_options(pathjson=self.path_json)
        except Exception as e:
            self.controller.log.warn(
                f"Error loading | sys.argv[1]={self.path_json} | {type(e)} | {e}"
            )
            result = 1
        if result == 1:
            if self.controller.query.target == TARGET_CLIENT:
                self.path_json = self.path_client_json
            else:
                self.path_json = self.path_server_json
            result = self._load_options(pathjson=self.path_json)
            if result == 1:
                self._default_options(pathjson=self.path_json)
        return result

    def _load_options(self, pathjson: str) -> int:
        self.controller.log.info(f"pathjson | {pathjson}")
        try:
            with open(pathjson, mode="r", encoding="windows-1251") as file_json:
                options_json = json.load(file_json)
            self._default_options(
                options_json=options_json,
                pathjson=pathjson,
            )
        except Exception as e:
            self.controller.log.warn(f"Error loading | {pathjson} | {type(e)} | {e}")
            return 1
        return 0

    def _default_options(self, options_json=None, pathjson=""):
        if pathjson == "":
            self.controller.log.warn(f"Path json is empty | pathjson'{pathjson}'")
            return 1
        if options_json is None:
            options_json = {
                "path_data": "data",
                "path_log": "log.txt",
                "savelable_log": 0,
            }
        try:
            self.path_data = options_json["path_data"]
            self.path_log = options_json["path_log"]
            self.savelable_log = options_json["savelable_log"]
            with open(pathjson, mode="w", encoding="windows-1251") as file_json:
                json.dump(options_json, file_json)
        except Exception as e:
            self.controller.log.error(
                f"Cannot set default options | {pathjson} | {type(e)} | {e}"
            )
            return 1
        return 0
