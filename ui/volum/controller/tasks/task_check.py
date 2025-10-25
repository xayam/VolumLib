from volum.controller.tasks.taskbase import TaskBase


class Check(TaskBase):

    def __init__(self):
        TaskBase.__init__(self)

    @staticmethod
    def check(self) -> str:
        super()._check(self)
        return self._do(self)

    def _do(self) -> str:
        return "Я проверяю. " + self.model.app_header()
