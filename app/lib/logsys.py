import logging
import sys

class Log:
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                        filename='../logs/muscle-orchestrator.log',
                        level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S')

    @classmethod
    def debug(cls, text):
        logging.debug(text)

    @classmethod
    def info(cls, text):
        logging.info(text)

    @classmethod
    def warning(cls, text):
        logging.warning(text)

    @classmethod
    def error(cls, text):
        logging.error(text)

    @classmethod
    def exit(cls):
        logging.info("-------------")
        logging.info("Terminating..")
        logging.info("-------------")
        sys.exit(2)