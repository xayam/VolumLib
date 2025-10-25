from volum.logger import Logger
from volum.controller.jobs import Jobs
from volum.model.model import Model
from volum.model.query import Query
from volum.view.view import View


class Controller:
    def __init__(
            self,
            jobs: Jobs,
            logger: Logger,
            model: Model,
            view: View,
            query: Query,
    ):
        self.jobs = jobs
        self.log = logger
        self.query = query
        self.model = model
        self.view = view
        self.log.model = self.model
        self.model.controller = self
        self.model.load_options()
        self.log._active = bool(self.model.savelable_log)
        self.view.controller = self
        self.view.model = self.model
        self.log.info(model.app_header())
        self.jobs.control(controller=self)

    def run(self) -> str:
        if self.query.jobs is None:
            return self.view.run()
        else:
            return self.jobs.do()
