from abc import ABCMeta
import logging

from statsd import StatsClient


logger = logging.getLogger(__name__)


class MetricsListener(object, metaclass=ABCMeta):
    """Base class for all the metrics listeners"""

    def incr(self, metric):
        """Increase the value of the given counter

        :param str metric: the metrics label
        """
        pass

    def timing(self, metric, value):
        """Set the value of the given timer

        :param str metric: the timer label
        :param float value: the time in seconds
        """
        pass

    def dispose(self):
        """Dispose the listener

        The implementations of the MetricsListener class should override this
        method in order to release the resources that the listener might hold.
        """


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

    def timing(self, metric, value):
        # statsd requires the time in milliseconds
        self._client.timing(metric, value * 1000)


class DummyMetricsListener(MetricsListener):
    def incr(self, metric):
        logger.info("increasing metric %s", metric)

    def timing(self, metric, value):
        logger.info("logging timing: %s=%s seconds", metric, value)
