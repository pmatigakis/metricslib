class Counter(object):
    """Counter metric"""

    def __init__(self, metrics, name):
        """Create a new Counter object

        :param metricslib.clients.Metrics metrics: the metrics client to use
        :param str name: the counter name
        """
        self._metrics = metrics
        self.name = name

    def incr(self):
        """Increase the counter"""
        self._metrics.incr(self.name)
