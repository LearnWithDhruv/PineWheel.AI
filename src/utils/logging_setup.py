import logging

def setup_logging():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("cybersec_rag")
    return logger
