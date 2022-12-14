import clickhouse_logging
import json
import logging
from logging import INFO
import random
import time
from datetime import datetime

now = datetime.now()

date_time = now.strftime("%Y-%m-%d")
print("date and time:",date_time)
logging.basicConfig(
    level="INFO",
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
)
logger = logging.getLogger(__name__)

CH_HTTP_INTERFACE = 'http://10.5.0.3:8123'

ch_logger = clickhouse_logging.getLogger(name=__name__,
                                         capacity=1000,  # capacity before send to CH
                                         filename='log.txt',  # optional,  if specified also send to local file
                                         level=INFO,
                                         ch_table='test.log',  # target CH table
                                         ch_conn=CH_HTTP_INTERFACE)


if __name__ == "__main__":
    while True:
        msg = dict()
        for level in range(50):
            (
                msg[f"bid_{str(level).zfill(2)}"],
                msg[f"ask_{str(level).zfill(2)}"],
            ) = (
                random.randrange(1, 100),
                random.randrange(100, 200),
            )
        msg["stats"] = {
            "sum_bid": sum(v for k, v in msg.items() if "bid" in k),
            "sum_ask": sum(v for k, v in msg.items() if "ask" in k),
        }
        #ch_logger.info(f"{json.dumps(msg)}")
        ch_logger.info('test', extra={'col': f"{json.dumps(msg)}", 'dt': f"{date_time}"})
        time.sleep(0.001)