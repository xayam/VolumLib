# from volum.Logger import Logger
import sys

from volum.controller.tasks.task_benchmarks import *
from volum.controller.tasks.task_check import *
from volum.controller.tasks.task_clean_dev import *
from volum.controller.tasks.task_search_dev import *
from volum.controller.tasks.task_translate_dev import *
from volum.controller.tasks.task_update_dev import *
from volum.controller.tasks.task_upload_dev import *

# from volum.controller.tasks.task_fts_dev import *

# from volum.controller.tasks.task_index_dev import *

# Logger().boot("<controller.tasks.__init__>")

sys.setrecursionlimit(2 ** 31 - 1)
