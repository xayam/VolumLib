from volum.const import *
from volum.i18l.messages import *

MESSAGES: dict = {
    INVALID_QUERY_INPUT_: u"Некорректный запрос",
    ERROR_CONTROLLER_IS_NOT_SET_: u"Контроллер не определён",
    ERROR_MODEL_IS_NOT_SET_: u"Модель не определена",
    SERVER_MODE_ENABLED_: u"Установлен режим сервера",
    CLIENT_MODE_ENABLED_: u"Установлен режим клиента",
    ERROR_NO_JOBS_: u"В запросе не определена работа",
    RESULT_RUN_IS_NONE_: u"Результат выполнения функции controller.run() равен None",
    COUNT_SKIP_ARCHIVES_: u"Количество пропущенных архивов: {}",
    LOADING_LIST_OF_TASK_: u"Загрузка списка имеющихся задач",
    TASKS_FOR_EXECUTING_: u"Список задач для исполнения: {}",
    TRANSLATE_COMPLETED_: u"Перевод на вторичные языки завершён",
    INVALID_TARGET_MODE_: u"Некорректный режим запуска",
    TARGET_UNKNOWN_: u"Цель неизвестна",
}
const_assert_list(const_key_dict_to_list(MESSAGES))
