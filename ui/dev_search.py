from build import Build
from volum.entity import *

if __name__ == "__main__":
    Build(
        release=False,
        jobs=[
            # TASK_TRANSLATE_DEV,
            # TASK_UPDATE_DEV,
            TASK_SEARCH_DEV,
            # TASK_BENCHMARKS,
        ],
    ).run()
