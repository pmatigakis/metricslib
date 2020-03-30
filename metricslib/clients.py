import logging

from metricslib.listeners import Listeners
from metricslib.metrics import Counter, Duration


logger = logging.getLogger(__name__)


class Metrics(object):
    """Metrics collection object"""

    def __init__(self):
        """Create a new Metrics object"""
        self._listeners = Listeners()

    def add_listener(self, listener):
        """Add a metrics listener

        :param MetricsListener listener: the listener object
        """
        self._listeners.add(listener)

    def clear_listeners(self):
        """Remove all the listeners"""
        self._listeners.clear()

    def counter(self, name):
        """Create a new counter

        :param str name: the counter name
        :rtype: Counter
        :return: the new counter object
        """
        return Counter(self._listeners, name)

    def dispose(self):
        """Dispose the metrics client and it's listeners"""
        self.clear_listeners()

    def duration(self, name):
        """Create a new duration metric

        :param str name: the duration metric  name
        :rtype: Duration
        :return: the new duration object
        """
        return Duration(self._listeners, name)

    def listener_count(self):
        """Get the number of listeners

        :rtype: int
        :return: the number of listeners
        """
        return self._listeners.count()
