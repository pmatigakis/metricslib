import logging

from metricslib.listeners import StatsdMetricsListener
from metricslib.utils import metrics


logger = logging.getLogger(__name__)


def configure_metrics_from_dict(config):
    """Configure the metrics client using data from the given dictionary

    :param dict config: the dictionary with the metrics configuration
    """
    logger.info("configuring metrics from dictionary data")

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
