import os
import datetime
import threading


class LogLevel:
    INFO = "INFO"
    DEBUG = "DEBUG"
    WARNING = "WARNING"
    ERROR = "ERROR"


class Logger:
    LOG_DIR = "./output/logs"
    _lock = threading.Lock()

    os.makedirs(LOG_DIR, exist_ok=True)

    file_name = None

    @classmethod
    def start_test(cls, test_nodeid: str):
        safe_name = test_nodeid.replace("::", "__").replace("/", "_").replace(" ", "_")
        cls.file_name = f"{cls.LOG_DIR}/log_{safe_name}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
        cls.info(f"=== START TEST: {test_nodeid} ===")

    @classmethod
    def write_log_to_file(cls, data: str, level: str = LogLevel.INFO):
        if cls.file_name is None:
            return
        if "test_result" in cls.file_name:
            raise ValueError(
                "Logger is trying to write to test_result. Check configuration!"
            )
        log_line = f"[{level}] {datetime.datetime.now().isoformat()} - {data}\n"
        with cls._lock:
            with open(cls.file_name, "a", encoding="utf-8") as logger_file:
                logger_file.write(log_line)

    @classmethod
    def info(cls, message: str):
        cls.write_log_to_file(message, level=LogLevel.INFO)

    @classmethod
    def debug(cls, message: str):
        cls.write_log_to_file(message, level=LogLevel.DEBUG)

    @classmethod
    def warning(cls, message: str):
        cls.write_log_to_file(message, level=LogLevel.WARNING)

    @classmethod
    def error(cls, message: str):
        cls.write_log_to_file(message, level=LogLevel.ERROR)

    @classmethod
    def add_request(cls, url: str, method: str, body=None, files_meta=None):
        test_name = os.environ.get("PYTEST_CURRENT_TEST", "unknown_test")
        data_to_add = "\n-----\n"
        data_to_add += f"Test:  {test_name}\n"
        data_to_add += f"Time:  {datetime.datetime.now().isoformat()}\n"
        data_to_add += f"Request method:  {method}\n"
        data_to_add += f"Request URL:  {url}\n"
        if body is not None:
            data_to_add += f"Request body: {body}\n"
        cls.debug(data_to_add)

    @classmethod
    def add_response(
        cls, response, body=None, endpoint_name: str = None, files_meta=None
    ):
        data_to_add = ""
        if endpoint_name:
            data_to_add += f"Endpoint: {endpoint_name}\n"
        data_to_add += f"Response status: {getattr(response, 'status_code', 'N/A')}\n"
        data_to_add += f"Response body: {getattr(response, 'text', str(response))}\n"
        if body is not None:
            data_to_add += f"Request body: {body}\n"
        data_to_add += "-----\n"
        if getattr(response, "status_code", 0) >= 400:
            cls.error(data_to_add)
        else:
            cls.info(data_to_add)
