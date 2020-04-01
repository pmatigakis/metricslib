from time import sleep

from metricslib.config import configure_from_dict
from metricslib.utils import get_metrics


def main():
    config = {
        "STATSD_HOST": "localhost",
        "STATSD_PORT": 8125
    }

    configure_from_dict(config)

    metrics = get_metrics()
    duration = metrics.duration("myapp.time")

    duration_measurement = duration.begin()
    sleep(2.0)
    duration_measurement.end()


if __name__ == "__main__":
    main()
