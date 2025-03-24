import logging
from time import sleep

from redis import Redis
from rq import Queue
from worker import count_words_at_url


logger = logging.getLogger("RQ Queue")


def queue_redis():
    # задаём соединение с Redis по умолчанию
    redis_conn = Redis(
        host='localhost',
        port=6379,
        db=0
    )
    q = Queue(
        name="high",
        connection=redis_conn,
    )

    r = Redis(
        host='localhost',
        port=6379,
        db=3,
        decode_responses=True,
    )

    p = r.pubsub()
    p.subscribe('test')

    # for _ in range(1, 10000):
    while True:
        try:
            # sleep(1)
            # job = q.enqueue(count_words_at_url, 'https://python-rq.org/', result_ttl=60)
            # logger.info(f"Job : {job}")

            message = p.get_message()
            if message is not None:
                print(message)
                # if message['channel'] == 'test':
                #     data = json.loads(message['data'])
                #     print(data)

                # кладём выполнение нашей задачи в очередь
                # job_1 = q.enqueue(count_words_at_url, 'https://khashtamov.com/')
                job = q.enqueue(count_words_at_url, 'https://python-rq.org/', result_ttl=60)
                logger.info(f"Job : {job}")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        queue_redis()
    except KeyboardInterrupt as ex:
        logger.info(f"Stop program")
