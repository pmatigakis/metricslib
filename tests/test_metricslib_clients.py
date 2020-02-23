from unittest import TestCase, main
from unittest.mock import MagicMock

from metricslib.clients import Metrics
from metricslib.listeners import DummyMetricsListener, StatsdMetricsListener


class MetricsTests(TestCase):
    def test_add_listener(self):
        metrics = Metrics()

        self.assertEqual(len(metrics._listeners), 0)

        listener = DummyMetricsListener()
        metrics.add_listener(listener)

        self.assertEqual(len(metrics._listeners), 1)

    def test_incr(self):
        metrics = Metrics()

        listener = DummyMetricsListener()
        listener.incr = MagicMock()
        metrics.add_listener(listener)

        metrics.incr("dummy.metric")

        listener.incr.assert_called_once_with("dummy.metric")

    def test_timing(self):
        metrics = Metrics()

        listener = DummyMetricsListener()
        listener.timing = MagicMock()
        metrics.add_listener(listener)

        metrics.timing("dummy.timing", 123.0)

        listener.timing.assert_called_once_with("dummy.timing", 123.0)


class StatsdMetricsListenerTests(TestCase):
    def test_incr(self):
        client = MagicMock()
        listener = StatsdMetricsListener(client)

        listener.incr("test.metric")

        client.incr.assert_called_once_with("test.metric")

    def test_timing(self):
        client = MagicMock()
        listener = StatsdMetricsListener(client)

        listener.timing("test.metric", 123.0)

        client.timing.assert_called_once_with("test.metric", 123000.0)


if __name__ == "__main__":
    main()
