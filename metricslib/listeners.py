from abc import ABCMeta
import logging

from statsd import StatsClient


logger = logging.getLogger(__name__)


class Listeners(object):
    """Listener container"""

    def __init__(self):
        """Create a new Listeners object"""
        self._listeners = set()

    def add(self, listener):
        """Add a listener to the container

        :param MetricsListener listener: the listener  to add
        """
        self._listeners.add(listener)

    def clear(self):
        """Remove all the listeners"""
        for listener in self._listeners:
            listener.dispose()

        self._listeners = set()

    def count(self):
        """Get the number of listeners

        :rtype: int
        :return: the number of listeners
        """
        return len(self._listeners)

    def incr(self, metric):
        """Increase the value of the given counter

        :param str metric: the metrics label
        """
        for listener in self._listeners:
            listener.incr(metric)

    def duration(self, metric, value):
        """Set the value of the given duration

        :param str metric: the timer label
        :param float value: the time in seconds
        """
        for listener in self._listeners:
            listener.duration(metric, value)


class MetricsListener(object, metaclass=ABCMeta):
    """Base class for all the metrics listeners"""

    def incr(self, metric):
        """Increase the value of the given counter

        :param str metric: the metrics label
        """
        pass

    def duration(self, metric, value):
        """Set the value of the given duration

        :param str metric: the timer label
        :param float value: the time in seconds
        """
        pass

    def dispose(self):
        """Dispose the listener

        The implementations of the MetricsListener class should override this
        method in order to release the resources that the listener might hold.
        """
        pass


class StatsdMetricsListener(MetricsListener):
    """Statsd metrics listener implementation"""

    def __init__(self, client):
        """Create a new StatsdMetricsListener object

        :param StatsClient client: the statsd client
        """
        self._client = client

    @classmethod
    def create_from_address(cls, host, port=8125):
        """Create a new listener object

        :param str host: the statsd server address
        :param int port: the statsd server port
        :rtype: StatsdMetricsListener
        :return: the new listener object
        """
        client = StatsClient(host, port)

        return cls(client)

    def incr(self, metric):
        self._client.incr(metric)

    def duration(self, metric, value):
        # statsd requires the time in milliseconds
        self._client.timing(metric, value * 1000)


class DummyMetricsListener(MetricsListener):
    def incr(self, metric):
        logger.info("increasing metric %s", metric)

    def duration(self, metric, value):
        logger.info("logging timing: %s=%s seconds", metric, value)
