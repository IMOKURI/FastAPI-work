import logging


class Common:
    def __init__(self):
        self.name = "Common"
        self.logger = None

    def get_logger(self):
        if self.logger is None:
            self.logger = logging.getLogger("app")
            self.logger.info(f"Logger created by {__name__}")
        return self.logger
