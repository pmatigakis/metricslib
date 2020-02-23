import time


class MetricBase(object):
    def __init__(self, listeners, name):
        """Create a new metric object

        :param metricslib.listeners.Listeners: the listeners to use
        :param str name: the metric name
        """
        self._listeners = listeners
        self._name = name


class Counter(MetricBase):
    """Counter metric"""

    def incr(self):
        """Increase the counter"""
        self._listeners.incr(self._name)


class DurationMeasurement(object):
    """Duration measurement object"""
    def __init__(self, listeners, name, start_time):
        """Create a new DurationMeasurement object

        :param metricslib.listeners.Listeners: the listeners to use
        :param str name: the name of the duration to measure
        :param float start_time: the duration start time
        """
        self._listeners = listeners
        self._name = name
        self._start_time = start_time

    def end(self):
        """Mark the end of the duration

        :rtype: float
        :return: the duration in seconds
        """
        execution_time = time.perf_counter() - self._start_time
        self._listeners.duration(self._name, execution_time)

        return execution_time


class Duration(MetricBase):
    """Duration metric"""

    def __init__(self, listeners, name):
        """Create a new Duration object

        :param metricslib.listeners.Listeners: the listeners to use
        :param str name: the duration metric name
        """
        super(Duration, self).__init__(listeners, name)

    def begin(self):
        """
        Mark the beginning of the metric

        :rtype: DurationMeasurement
        :return: the duration measurement object
        """
        return DurationMeasurement(
            listeners=self._listeners,
            name=self._name,
            start_time=time.perf_counter()
        )
