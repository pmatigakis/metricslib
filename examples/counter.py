from metricslib.config import configure_metrics_from_dict
from metricslib.utils import get_metrics


def main():
    config = {
        "STATSD_HOST": "localhost",
        "STATSD_PORT": 8125
    }

    configure_metrics_from_dict(config)

    metrics = get_metrics()
    counter = metrics.counter("myapp.count")
    counter.incr()


if __name__ == "__main__":
    main()
