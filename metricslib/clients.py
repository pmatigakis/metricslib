import logging
from abc import ABCMeta, abstractmethod

from statsd import StatsClient


logger = logging.getLogger(__name__)


class MetricsListener(object):
    """Base class for all the metrics listeners"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def incr(self, metric):
        """Increase the value of the given counter

        :param str metric: the metrics label
        """
        pass

    @abstractmethod
    def timing(self, metric, value):
        """Set the value of the given timer

        :param str metric: the timer label
        :param int value: the time in milliseconds
        """
        pass


class StatsdMetricsListener(MetricsListener):
    """Statsd metrics listener implementation"""

    def __init__(self, host, port=8125):
        """Create a new StatsdMetricsListener object

        :param str host: the statsd server host
        :param int port: the statsd server port
        """
        self._client = StatsClient(host, port)

    def incr(self, metric):
        self._client.incr(metric)

    def timing(self, metric, value):
        self._client.timing(metric, value)


class DummyMetricsListener(MetricsListener):
    def incr(self, metric):
        logger.info("increasing metric %s", metric)

    def timing(self, metric, value):
        logger.info("logging timing: %s=%s", metric, value)


class Metrics(object):
    """Metrics collection object"""

    def __init__(self):
        """Create a new Metrics object"""
        self._listeners = []

    def add_listener(self, listener):
        """Add a metrics listener

        :param MetricsListener listener: the listener object
        """
        self._listeners.append(listener)

    def incr(self, metric):
        """Increase the value of the given counter

        :param str metric: the metrics label
        """
        for listener in self._listeners:
            listener.incr(metric)

    def timing(self, metric, value):
        """Set the value of the given timer

        :param str metric: the timer label
        :param int value: the time in milliseconds
        """
        for listener in self._listeners:
            listener.timing(metric, value)
