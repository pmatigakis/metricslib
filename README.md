Metricslib is a package that can be used to send application metrics to metric
collections services.

##### Supported metric collection services

* [statsd](https://github.com/statsd/statsd)

## Installation

Metricslib requires python >= 3.5. Install the latest version from the github
repository

```bash
pip install git+https://github.com/topicaxis/metricslib.git@v0.1.0 
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
