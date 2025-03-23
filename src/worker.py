import logging
from random import randint
from time import sleep

import httpx


def count_words_at_url(url):
    # rand_int = randint(1, 10)
    # sleep(rand_int)
    # print(f"i sleep for {rand_int} seconds")
    # return rand_int

    # resp = httpx.get(url)
    # sleep(0.5)
    logger = logging.getLogger("RQ Queue")
    msg = f"i'm working! *******************"
    logger.info(msg)
    return msg

    # logger.info(f"Response code: {resp.status_code}")
    # return len(resp.text.split())
