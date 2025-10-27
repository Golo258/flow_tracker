
import logging
import sys
from pathlib import Path
from typing import Optional

class LoggerManager:
    """
    Lightweight logging utility with console and file output.
    """

    _logger: Optional[logging.Logger] = None
    _file_handler: Optional[logging.FileHandler] = None
    _log_dir: Optional[Path] = None

    @classmethod
    def configure(
        cls,
        name: str = "focusflow",
        log_dir: Optional[str | Path] = None,
        level: int = logging.INFO,
        console: bool = True,
    ) -> None:
        """
        Configure the base logger.

        :param name: Logger name
        :param log_dir: Directory to store log file (optional)
        :param level: Logging level
        :param console: Whether to log to console
        """
        if cls._logger:
            return  # already configured

        cls._logger = logging.getLogger(name)
        cls._logger.setLevel(level)
        cls._logger.propagate = False

        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S.%f",
        )

        if console:
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setFormatter(cls._colorize_formatter(formatter))
            cls._logger.addHandler(console_handler)

        if log_dir:
            Path(log_dir).mkdir(parents=True, exist_ok=True)
            log_file = Path(log_dir) / f"{name}.log"
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setFormatter(formatter)
            cls._logger.addHandler(file_handler)
            cls._file_handler = file_handler
            cls._log_dir = Path(log_dir)

        cls._logger.debug("Logger configured")

    @classmethod
    def _colorize_formatter(cls, formatter: logging.Formatter) -> logging.Formatter:
        """
        Wrap formatter to colorize log levels.
        """
        COLORS = {
            "DEBUG": "\033[37m",     # gray
            "INFO": "\033[36m",      # cyan
            "WARNING": "\033[33m",   # yellow
            "ERROR": "\033[31m",     # red
            "CRITICAL": "\033[41m",  # red background
        }
        RESET = "\033[0m"

        class ColorFormatter(logging.Formatter):
            def format(self, record: logging.LogRecord) -> str:
                levelname = record.levelname
                msg = formatter.format(record)
                color = COLORS.get(levelname, "")
                return f"{color}{msg}{RESET}"

        return ColorFormatter(formatter._fmt, formatter.datefmt)

    @classmethod
    def log_msg(cls, msg: str, lvl: str = "INFO", to_console: bool = False) -> None:
        """
        Log a message at a given level.

        :param msg: message string
        :param lvl: log level name (INFO, WARNING, ERROR, DEBUG)
        :param to_console: if True, ensures message also goes to stdout
        """
        if not cls._logger:
            cls.configure()  # default setup if not yet configured

        level = lvl.upper()
        log_func = getattr(cls._logger, level.lower(), cls._logger.info)
        log_func(msg)

        if to_console:
            print(msg)

    @classmethod
    def close(cls) -> None:
        """
        Close file handler if open.
        """
        if cls._file_handler:
            cls._logger.removeHandler(cls._file_handler)
            cls._file_handler.close()
            cls._file_handler = None
            cls._log_dir = None

