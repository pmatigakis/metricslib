import logging

from metricslib.utils import get_metrics


logger = logging.getLogger(__name__)
metrics = get_metrics()


def capture_metrics(request_metric, error_metric, success_metric,
                    execution_time_metric):
    """Capture metrics for this endpoint

    :param request_metric: the label to use for the request counter
    :param error_metric: the label to use for the error counter
    :param success_metric: the label to use for the success counter
    :param execution_time_metric: the label to use for the request execution
        timer
    """
    request_counter = metrics.counter(request_metric)
    success_counter = metrics.counter(success_metric)
    error_counter = metrics.counter(error_metric)
    execution_time_duration = metrics.duration(execution_time_metric)

    def endpoint_wrapper(f):
        def wrapper(*args, **kwargs):
            logger.info("collecting metrics")

            request_counter.incr()
            duration_measurement = execution_time_duration.begin()

            try:
                response = f(*args, **kwargs)
            except Exception as e:
                error_counter.incr()
                raise e

            duration_measurement.end()
            success_counter.incr()

            return response
        return wrapper
    return endpoint_wrapper
