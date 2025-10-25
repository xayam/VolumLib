from volum.controller.tasks.taskbase import TaskBase


class UploadDev(TaskBase):

    def __init__(self):
        TaskBase.__init__(self)

    @staticmethod
    def upload_dev(self) -> str:
        super()._check(self)
        return self._do(self)

    def _do(self) -> str:
        return "Я публикую закачивая на сервер. " + self.model.app_header()
