import logging


class Common:
    def __init__(self):
        self.name = "Common"
        self.logger = None

    def get_logger(self):
        if self.logger is None:
            print("Create logger")
            self.logger = logging.getLogger(__name__)
            self.logger.info("Logger created")
        return self.logger
