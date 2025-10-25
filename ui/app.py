from bootstrap import *
from volum import *

from volum.controller.controller import Controller
from volum.controller.jobs import Jobs
from volum.logger import Logger
from volum.i18l.i18l import I18L
from volum.i18l.messages import *
from volum.model.model import Model
from volum.model.query import Query
from volum.view.view import View


class App:

    def __init__(self, query: Query):
        self.query = query

    def run(self) -> int:
        i18l = I18L(language=self.query.language)
        if not isinstance(self.query, Query):
            raise ValueError(i18l.t(INVALID_QUERY_INPUT_))
        model = Model(i18l=i18l)
        view = View()
        logger = Logger()

        jobs = Jobs(logger)
        controller = Controller(
            jobs=jobs, logger=logger, model=model, view=view, query=self.query
        )
        controller.model.set_target(self.query.target)
        controller.log.info(i18l.t(TASKS_FOR_EXECUTING_).format(self.query.jobs))

        try:
            result = controller.run()
            if result is not None:
                controller.log.info(result)
            else:
                controller.log.warn(i18l.t(RESULT_RUN_IS_NONE_))
        except Exception as e:
            # if not self.query.release:
            controller.log.error(f"{type(e)} : {e}")
            return 1
        return 0


def main() -> int:
    application = App(
        Query(
            release=False,
            jobs=[],
            target=TARGET_CLIENT,
            language=LANG_PRIMARY,
        )
    )
    return application.run()


if __name__ == "__main__":
    main()
