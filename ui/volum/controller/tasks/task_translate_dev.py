from volum.controller.tasks.taskbase import TaskBase
from volum.i18l.messages import *


class TranslateDev(TaskBase):

    def __init__(self):
        TaskBase.__init__(self)

    @staticmethod
    def translate_dev(self) -> str:
        super()._check(self)
        return self._do(self)

    def _do(self) -> str:
        self.model.i18l.translate()
        # self.model.i18l.set_language(ENG)
        return self.model.i18l.t(TRANSLATE_COMPLETED_)
