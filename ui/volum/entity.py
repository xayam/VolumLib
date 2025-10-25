RUS: str = "ru"
ENG: str = "en"

LANG_PRIMARY: str = RUS
LANG_SECONDARY: list = [
    ENG,
]
PATH_LANG = "volum.i18l.i18l_"
TORRENTPATH: str = "VolumLib"
CLIENTNAME = "Portable-Client-VolumLib"
SERVERNAME = "Portable-Server-VolumLib"
MESSAGES: str = "MESSAGES"
BOOTSTRAP: str = "Bootstrap"

INFO: str = "info"
PINFO: str = "pinfo"
WARN: str = "warn"
ERROR: str = "error"
DEBUG: str = "debug"
BOOT: str = "boot"

VERSION_DEFAULT: str = "unknown"

LOG: dict = {
    INFO: "[INFO ]",
    PINFO: "[PINFO]",
    WARN: "[WARN ]",
    ERROR: "[ERROR]",
    DEBUG: "[DEBUG]",
    BOOT: "[BOOT ]",
}

TASK_BENCHMARKS: str = "benchmarks"
TASK_CHECK: str = "check"
TASK_CLEAN_DEV: str = "clean_dev"
TASK_SEARCH_DEV: str = "search_dev"
TASK_TRANSLATE_DEV: str = "translate_dev"
TASK_UPDATE_DEV: str = "update_dev"
TASK_UPLOAD_DEV: str = "upload_dev"

TARGET_DEV: str = "development"
TARGET_CLIENT: str = "client"
TARGET_SERVER: str = "server"

TARGETS = (TARGET_DEV, TARGET_CLIENT, TARGET_SERVER)
