

from common.logger import LoggerManager

def main():
    logger: LoggerManager = LoggerManager()
    logger.log_msg("\n", lvl="INFO")
    logger.log_msg("Starting planner", lvl="INFO")
    logger.log_msg("FIle not found", lvl="WARNING", to_console=True)

if __name__ == "__main__":
    main()