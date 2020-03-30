from unittest import TestCase, main
from unittest.mock import MagicMock

from metricslib.listeners import (
    Listeners, DummyMetricsListener, StatsdMetricsListener,
    LoggerMetricsListener
)


class ListenerTests(TestCase):
    def test_incr(self):
        listener = DummyMetricsListener()
        listener.incr = MagicMock()
        listeners = Listeners()
        listeners.add(listener)

        listeners.incr("dummy.metric")

        listener.incr.assert_called_once_with("dummy.metric")

    def test_timing(self):
        listener = DummyMetricsListener()
        listener.duration = MagicMock()
        listeners = Listeners()
        listeners.add(listener)

        listeners.duration("dummy.timing", 123.0)

        listener.duration.assert_called_once_with("dummy.timing", 123.0)


class StatsdMetricsListenerTests(TestCase):
    def test_incr(self):
        client = MagicMock()
        listener = StatsdMetricsListener(client)

        listener.incr("test.metric")

        client.incr.assert_called_once_with("test.metric")

    def test_timing(self):
        client = MagicMock()
        listener = StatsdMetricsListener(client)

        listener.duration("test.metric", 123.0)

        client.timing.assert_called_once_with("test.metric", 123000.0)


class LoggerMetricsListenerTests(TestCase):
    def test_incr(self):
        logger = MagicMock()
        listener = LoggerMetricsListener(logger)

        listener.incr("test.metric")

        logger.info.assert_called_once_with(
            "increasing metric: %s=%s", "test.metric", 1)

    def test_timing(self):
        logger = MagicMock()
        listener = LoggerMetricsListener(logger)

        listener.duration("test.metric", 123.0)

        logger.info.assert_called_once_with(
            "logging timing: %s=%s seconds", "test.metric", 123.0)


if __name__ == "__main__":
    main()
