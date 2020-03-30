from unittest import TestCase, main

from metricslib.config import create_listeners_from_configuration
from metricslib.listeners import StatsdMetricsListener, LoggerMetricsListener


class CreateListenersFromConfigurationTests(TestCase):
    def test_create_listeners_from_configuration(self):
        config = {
            "STATSD_HOST": "192.168.1.1",
            "LOGGER": "mylogger"
        }

        listeners = create_listeners_from_configuration(config)

        self.assertEqual(len(listeners), 2)
        self.assertIsInstance(listeners[0], StatsdMetricsListener)
        self.assertIsInstance(listeners[1], LoggerMetricsListener)


if __name__ == "__main__":
    main()
