from metricslib.utils import configure_metrics_from_dict
from metricslib.decorators import capture_metrics


@capture_metrics(
    request_metric="metricslib.test.request",
    error_metric="metricslib.test.error",
    success_metric="metricslib.test.success",
    execution_time_metric="metricslib.test.execution"
)
def do_something():
    print("hello world")


@capture_metrics(
    request_metric="metricslib.test.request",
    error_metric="metricslib.test.error",
    success_metric="metricslib.test.success",
    execution_time_metric="metricslib.test.execution"
)
def do_something_bad():
    # raise an exception
    raise Exception()


def main():
    config = {
        "STATSD_HOST": "localhost",
        "STATSD_PORT": 8125
    }

    configure_metrics_from_dict(config)

    do_something()

    # we want this function to raise an exception in order to test the error
    # metric
    do_something_bad()


if __name__ == "__main__":
    main()
