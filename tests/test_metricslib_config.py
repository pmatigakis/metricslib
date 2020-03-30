from unittest import TestCase, main

from metricslib.config import create_listeners_from_configuration
from metricslib.listeners import StatsdMetricsListener


class CreateListenersFromConfigurationTests(TestCase):
    def test_create_listeners_from_configuration(self):
        config = {
            "STATSD_HOST": "192.168.1.1"
        }

        listeners = create_listeners_from_configuration(config)

        self.assertEqual(len(listeners), 1)
        self.assertIsInstance(listeners[0], StatsdMetricsListener)


if __name__ == "__main__":
    main()
