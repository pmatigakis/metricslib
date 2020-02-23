from unittest import TestCase, main

from metricslib.clients import Metrics
from metricslib.listeners import DummyMetricsListener


class MetricsTests(TestCase):
    def test_add_listener(self):
        metrics = Metrics()

        self.assertEqual(metrics.listener_count(), 0)

        listener = DummyMetricsListener()
        metrics.add_listener(listener)

        self.assertEqual(metrics.listener_count(), 1)


if __name__ == "__main__":
    main()
