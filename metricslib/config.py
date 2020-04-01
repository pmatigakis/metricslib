import logging

from metricslib import _metrics
from metricslib.listeners import StatsdMetricsListener, LoggerMetricsListener


logger = logging.getLogger(__name__)


def create_listeners_from_configuration(config):
    """Create the listeners using the given configuration

    :param dict config: the metrics configuration
    :rtype: list[metricslib.listeners.MetricsListener]
    :return: the metrics listeners
    """
    listeners = []

    if "STATSD_HOST" in config:
        statsd_host = config.get("STATSD_HOST")
        statsd_port = config.get("STATSD_PORT", 8125)

        logger.info(
            "using statsd metrics listener: host=%s port=%s",
            statsd_host, statsd_port
        )

        listeners.append(StatsdMetricsListener.create_from_address(
            host=statsd_host,
            port=statsd_port
        ))

    if "LOGGER" in config:
        listeners.append(LoggerMetricsListener(
            logging.getLogger(config["LOGGER"])))

    return listeners


def configure_from_dict(config, clear_existing_listeners=True):
    """Configure the metrics client using data from the given dictionary

    :param dict config: the dictionary with the metrics configuration
    :param boolean clear_existing_listeners: remove the existing listeners
    """
    logger.info("configuring metrics from dictionary data")

    if clear_existing_listeners:
        logger.info("removing all existing listeners")
        _metrics.clear_listeners()

    listeners = create_listeners_from_configuration(config)

    for listener in listeners:
        _metrics.add_listener(listener)
