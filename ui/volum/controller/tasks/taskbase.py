from abc import ABCMeta

from volum.entity import *
from volum.i18l.messages import *
from volum.i18l.i18l_ru import MESSAGES


class TaskBase(metaclass=ABCMeta):

    def __init__(self):
        self.controller = None
        self.model = None

    @staticmethod
    def _check(self):
        if self.controller is None:
            raise ValueError(MESSAGES[ERROR_CONTROLLER_IS_NOT_SET_])
        if self.model is None:
            raise ValueError(MESSAGES[ERROR_MODEL_IS_NOT_SET_])
