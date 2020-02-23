class MetricslibError(Exception):
    """Base metricslib exception"""
    pass


class DurationError(MetricslibError):
    """Exception raised when there was an error when calculating a duration"""
    pass
