from volum.controller.tasks.taskbase import TaskBase
from volum.model.multistorage import MultiStorage


class SearchDev(TaskBase):

    def __init__(self):
        TaskBase.__init__(self)

    @staticmethod
    def search_dev(self) -> int:
        super()._check(self)
        return self._do(self)

    def _do(self) -> int:
        self.model.db = MultiStorage(path=f"{self.model.path_data}/fm", )
        return self.model.db.search()
