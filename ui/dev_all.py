from app import App

from volum.entity import *
from volum.model.query import Query


def main() -> int:
    application = App(
        Query(
            jobs=[
                TASK_TRANSLATE_DEV,
                TASK_UPDATE_DEV,
                TASK_UPLOAD_DEV,
                TASK_CHECK,
                TASK_CLEAN_DEV,
                TASK_BENCHMARKS,
            ],
            target=TARGET_SERVER,
            language=RUS,
        )
    )
    application.run()
    return 0


if __name__ == "__main__":
    main()
