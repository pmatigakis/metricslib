import logging

from metricslib.metrics import Counter, Duration


logger = logging.getLogger(__name__)


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

    def clear_listeners(self):
        """Remove all the listeners"""
        for listener in self._listeners:
            listener.dispose()

        self._listeners = []

    def counter(self, name):
        """Create a new counter

        :param str name: the counter name
        :rtype: Counter
        :return: the new counter object
        """
        return Counter(self, name)

    def duration(self, name):
        """Create a new duration metric

        :param str name: the duration metric  name
        :rtype: Duration
        :return: the new duration object
        """
        return Duration(self, name)

    def incr(self, metric):
        """Increase the value of the given counter

        :param str metric: the metrics label
        """
        for listener in self._listeners:
            listener.incr(metric)

    def timing(self, metric, value):
        """Set the value of the given timer

        :param str metric: the timer label
        :param float value: the time in seconds
        """
        for listener in self._listeners:
            listener.timing(metric, value)
