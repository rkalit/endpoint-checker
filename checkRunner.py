from time import time, sleep
from checkEP import *

while True:
    sleep(60 - time() % 60)
    checkEndpoint()
