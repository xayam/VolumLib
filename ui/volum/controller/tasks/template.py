from volum.controller.tasks.taskbase import TaskBase


class Template(TaskBase):

    def __init__(self):
        TaskBase.__init__(self)

    @staticmethod
    def template(self) -> str:
        super()._check(self)
        return self._do(self)

    def _do(self) -> str:
        return "Я шаблон. " + self.model.app_header()
