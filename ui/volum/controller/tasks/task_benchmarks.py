import random

from volum.controller.tasks.taskbase import TaskBase


class Benchmarks(TaskBase):

    def __init__(self):
        TaskBase.__init__(self)

    @staticmethod
    def benchmarks(self, query=None) -> dict:
        super()._check(self)
        for _ in range(1):
            self._do(self, query=query)
        return {}

    def _do(self, query=None) -> dict:
        if query is None:
            query = [
                # " атеросклероз и артериальная гипертония Противопоказания выраженные",
                # " Жираф и тушканчик",
                " Сказка о Методе",
                # " словарь",
                # " Справочник по оказанию скорой и неотложной помощи",
                # " gggggggg",
                # " перепоручить",
                # " llllllllll",
                # "огород участок",
            ]
            random.shuffle(query)
            query = query[0]
        return self.model.db.task_benchmarks(query=query)
