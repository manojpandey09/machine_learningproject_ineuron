from sensor.exception import sensorException
import os
import sys
from sensor.logger import logging

def test_exception():
    try:
        logging.info("kesa chlra h ")
        a = 1 / 0
    except Exception as e:
        raise sensorException(e, sys)
    



if __name__ == "__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)