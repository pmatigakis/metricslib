Metricslib is a package that can be used to send application metrics to metric
collections services.

##### Supported metric collection services

* [statsd](https://github.com/statsd/statsd)

## Installation

Metricslib requires python >= 3.5. Install the latest version using pip

```bash
pip install metricslib 
```

## Usage

Metricslib provides a decorator that can be used on a function where we want to
collect metrics about how many times it was called, how many times it executed
successfully, how many times it was executed with errors and how long it took
to run.

For the moment the only supported metric collection service is Statsd.

```python
from metricslib.utils import configure_metrics_from_dict
from metricslib.decorators import capture_metrics

@capture_metrics(
    request_metric="myapp.do_something.request",
    error_metric="myapp.do_something.error",
    success_metric="myapp.do_something.success",
    execution_time_metric="myapp.do_something.execution"
)
def do_something():
    print("hello world")


@capture_metrics(
    request_metric="myapp.do_something.request",
    error_metric="myapp.do_something.error",
    success_metric="myapp.do_something.success",
    execution_time_metric="myapp.do_something.execution"
)
def do_something_bad():
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

```

Instead of using the decorator you can create counter objects.

```python
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
```

You can also measure the time duration of an operation.

```python
from time import sleep

from metricslib.config import configure_metrics_from_dict
from metricslib.utils import get_metrics


def main():
    config = {
        "STATSD_HOST": "localhost",
        "STATSD_PORT": 8125
    }

    configure_metrics_from_dict(config)

    metrics = get_metrics()
    duration = metrics.duration("myapp.time")

    duration_measurement = duration.begin()
    sleep(2.0)
    duration_measurement.end()


if __name__ == "__main__":
    main()

```
