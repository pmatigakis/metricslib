import time
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
    def endpoint_wrapper(f):
        def wrapper(self, req, resp, *args, **kwargs):
            logger.info("collecting metrics")

            request_start_time = time.perf_counter()
            metrics.incr(request_metric)

            try:
                response = f(self, req, resp, *args, **kwargs)
            except Exception as e:
                metrics.incr(error_metric)
                raise e

            metrics.incr(success_metric)

            execution_time = time.perf_counter() - request_start_time
            metrics.timing(execution_time_metric, execution_time * 1000)

            return response
        return wrapper
    return endpoint_wrapper
