import os

from volum.entity import *
from volum.i18l.i18l import I18L
from volum.i18l.messages import *
from volum.model.config import Config


class Model(Config):
    _target = None
    _dev: bool = False
    _server: bool = False
    _client: bool = False
    controller: None
    db = None

    def __init__(self, i18l: I18L):
        self.i18l = i18l
        Config.__init__(self)

    def _init(self):
        if self.is_dev():
            if os.path.exists(self.path_temp):
                if not os.path.exists(self.path_temp_txt):
                    os.mkdir(self.path_temp_txt)
            else:
                self.controller.log.error(
                    f"Не найдена временная папка | {self.path_temp}"
                )

    def _mode_server(self):
        self._dev = False
        self._server = True
        self._client = False

    def _mode_client(self):
        self._dev = False
        self.server = False
        self._client = True

    def _mode_dev(self):
        self._dev = True
        self._server = False
        self._client = False

    def set_target(self, target: str):
        self._target = target
        if self._target == TARGET_SERVER:
            self._mode_server()
            self.controller.log.info(self.i18l.t(SERVER_MODE_ENABLED_))
        elif self._target == TARGET_CLIENT:
            self._mode_client()
            self.controller.log.info(self.i18l.t(CLIENT_MODE_ENABLED_))
        elif self._target == TARGET_DEV:
            self._mode_dev()
            self.controller.log.info("Установлен режим разработчика")
        else:
            raise Exception(
                self.controller.log.error(self.i18l.t(INVALID_TARGET_MODE_))
            )
        self._init()
        self.db = None  # Storage(controller=self.controller)

    def is_dev(self) -> bool:
        return self._dev

    def is_server(self) -> bool:
        return self._server

    def is_client(self) -> bool:
        return self._client
