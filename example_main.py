from html_logger import HTMLDetailsFormatter
import logging


# setup html logger only for errors
HTMLDetailsFormatter.initLogger(output='logs/errors.html')

# all others log as plain text
logger = logging.getLogger('html_details_logger')
info_handler = logging.FileHandler('info.log', mode='w', encoding='utf-8')
info_handler.setLevel(logging.INFO)
info_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
info_handler.setFormatter(info_formatter)
logger.addHandler(info_handler)


# example output
logger.debug("Message for DEBUG")
logger.info("Message for INFO")
logger.error("Message for ERROR")