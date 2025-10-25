import importlib

from volum import entity
from volum.controller.tasks import *


class Jobs:
    task_dir: str = "volum.controller.tasks"
    controller = None
    model = None
    tasks_dict: dict = {}

    def __init__(self, logger=None, task_dir: str = task_dir):
        self.log = logger
        self.task_dir = task_dir

    def do(self) -> str:
        for task in self.controller.query.jobs:
            if not self.model.is_dev() and task.endswith("_dev"):
                self.log.warn("Доступ запрещён: {}".format(task))
                continue
            self.log.info(f"Задача | {task}")
            call = getattr(self.tasks_dict[task], task)
            message = str(call(self.tasks_dict[task]))
            self.log.info(message)
        return "0"

    def control(self, controller) -> None:
        self.controller = controller
        self.model = controller.model
        self.tasks_dict = self._init_dict()
        for key in self.tasks_dict:
            self.tasks_dict[key].controller = self.controller
            self.tasks_dict[key].model = self.model

    def _init_dict(self) -> dict:
        tasks: list = [
            task[5:].lower()
            for task in dir(entity)
            if task.upper() == task and task.startswith("TASK_")
        ]
        result: dict = {}
        if self.log is not None and self.model is not None:
            self.log.info(self.model.i18l.t(LOADING_LIST_OF_TASK_))
        for task in tasks:
            # self.log.info(task)
            result[task] = getattr(
                importlib.import_module(
                    self.task_dir.replace("/", ".") + ".task_" + task
                ),
                task.capitalize().replace("_dev", "Dev"),
            )
        return result
