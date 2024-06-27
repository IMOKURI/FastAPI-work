import logging


class Common:
    def __init__(self):
        self.name = "Common"
        self.logger = None

    def get_logger(self):
        if self.logger is None:
            print("Create logger")
            # logging.filename = "app.log"
            # logging.config.fileConfig("logging.conf")
            self.logger = logging.getLogger(__name__)
            # self.logger = logging.getLogger("uvicorn.app")
        return self.logger
