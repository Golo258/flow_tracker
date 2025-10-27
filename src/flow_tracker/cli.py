

from common.logger import LoggerManager
from services.task_service import add_new_task

def main():
    logger: LoggerManager = LoggerManager()
    logger.log_msg("\n", lvl="INFO")
    logger.log_msg("Starting planner", lvl="INFO")
    logger.log_msg("FIle not found", lvl="WARNING", to_console=True)

    tasks = add_new_task(
        "Create structure",
        7,
        "Create base structure for project"
    )
    logger.log_msg(tasks, to_console=True)


if __name__ == "__main__":
    main()