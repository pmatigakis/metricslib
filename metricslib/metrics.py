import time

from metricslib.exceptions import DurationError


class MetricBase(object):
    def __init__(self, metrics, name):
        """Create a new metric object

        :param metricslib.clients.Metrics metrics: the metrics client to use
        :param str name: the metric name
        """
        self._metrics = metrics
        self.name = name


class Counter(MetricBase):
    """Counter metric"""

    def incr(self):
        """Increase the counter"""
        self._metrics.incr(self.name)


class Duration(MetricBase):
    """Duration metric"""

    def __init__(self, metrics, name):
        """Create a new Duration object

        :param metricslib.clients.Metrics metrics: the metrics client to use
        :param str name: the duration metric name
        """
        super(Duration, self).__init__(metrics, name)

        self._start = None

    def begin(self):
        """Mark the beginning of the metric"""
        self._start = time.perf_counter()

    def end(self):
        """Mark the end of the metric

        :rtype: float
        :return: the duration in seconds
        """
        if self._start is None:
            raise DurationError("The duration metric hasn't been started")

        execution_time = time.perf_counter() - self._start
        self._metrics.timing(self.name, execution_time)
        self._start = None

        return execution_time
