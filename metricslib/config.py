import logging

from metricslib.listeners import StatsdMetricsListener
from metricslib.utils import metrics


logger = logging.getLogger(__name__)


def configure_metrics_from_dict(config, clear_existing_listeners=True):
    """Configure the metrics client using data from the given dictionary

    :param dict config: the dictionary with the metrics configuration
    :param boolean clear_existing_listeners: remove the existing listeners
    """
    logger.info("configuring metrics from dictionary data")

    if clear_existing_listeners:
        logger.info("removing all existing listeners")
        metrics.clear_listeners()

    statsd_host = config.get("STATSD_HOST")
    statsd_port = config.get("STATSD_PORT", 8125)

    if statsd_host is not None:
        logger.info(
            "using statsd metrics listener: host=%s port=%s",
            statsd_host, statsd_port
        )

        listener = StatsdMetricsListener.create_from_address(
            host=statsd_host,
            port=statsd_port
        )

        metrics.add_listener(listener)
