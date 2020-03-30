from metricslib.clients import Metrics


metrics = Metrics()


def get_metrics():
    """Get the main Metrics object

    :rtype: Metrics
    :return: the main metrics object
    """
    return metrics
