from app import App

from volum.model.query import Query
from volum.entity import *


def main() -> int:
    application = App(
        Query(
            target=TARGET_CLIENT,
            language=LANG_PRIMARY,
        )
    )
    application.run()
    return 0


if __name__ == "__main__":
    main()
