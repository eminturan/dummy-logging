import logging
import time

# Create a log message
logging.basicConfig(
    filename='app.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

temp = 1
while (True):
    logging.info("message %s", temp)
    temp += 1
    time.sleep(5)
