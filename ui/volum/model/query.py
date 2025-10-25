from volum.entity import *


class Query:
    def __init__(
        self,
        release=False,
        jobs=None,
        target=TARGET_SERVER,
        language: str = LANG_PRIMARY,
    ):
        self.release = release
        self.jobs = jobs
        self.target = target
        self.language = language
