from volum.const import *
from volum.i18l.messages import *


MESSAGES: dict = {
        INVALID_QUERY_INPUT_: u"Incorrect request", 
        ERROR_CONTROLLER_IS_NOT_SET_: u"Controller's not defined", 
        ERROR_MODEL_IS_NOT_SET_: u"Model not defined", 
        SERVER_MODE_ENABLED_: u"Server mode established", 
        CLIENT_MODE_ENABLED_: u"Customer regime established", 
        ERROR_NO_JOBS_: u"The request does not specify the work", 
        RESULT_RUN_IS_NONE_: u"Result of function controller.run() equals None", 
        COUNT_SKIP_ARCHIVES_: u"Number of archives released: {}", 
        LOADING_LIST_OF_TASK_: u"Loading of list of existing tasks", 
        TASKS_FOR_EXECUTING_: u"List of tasks for implementation: {}", 
        TRANSLATE_COMPLETED_: u"Translation into secondary languages completed", 
        INVALID_TARGET_MODE_: u"Incorrect launch regime", 
        TARGET_UNKNOWN_: u"Target unknown", 
    }


const_assert_list(const_key_dict_to_list(MESSAGES))
