import unittest

from logging import (
    LogRecord,
    DEBUG,
    INFO,
    WARNING,
    ERROR,
    CRITICAL
)

from pytracelog.logger.handlers import StdoutHandler, StderrHandler

_LOGFORMAT = '[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s'
_DATEFORMAT = '%d-%m-%Y %H:%M:%S'


class TestHandlers(unittest.TestCase):
    def setUp(self) -> None:
        self.stdout_h = StdoutHandler()
        self.stderr_h = StderrHandler()
        self.log_debug = LogRecord(
            name='__main__',
            level=DEBUG,
            pathname='path/logger.py',
            lineno=76,
            msg='test debug',
            exc_info=None,
            args=()
        )
        self.log_info = LogRecord(
            name='__main__',
            level=INFO,
            pathname='path/logger.py',
            lineno=76,
            msg='test info',
            exc_info=None,
            args=()
        )
        self.log_warning = LogRecord(
            name='__main__',
            level=WARNING,
            pathname='path/logger.py',
            lineno=76,
            msg='test warning',
            exc_info=None,
            args=()
        )
        self.log_error = LogRecord(
            name='__main__',
            level=ERROR,
            pathname='path/logger.py',
            lineno=76,
            msg='test info',
            exc_info=None,
            args=()
        )

        self.log_critical = LogRecord(
            name='__main__',
            level=CRITICAL,
            pathname='path/logger.py',
            lineno=76,
            msg='test warning',
            exc_info=None,
            args=()
        )

    def test_stdout_handlers_true(self):
        self.assertTrue(self.stdout_h.error_record_filter(self.log_debug))
        self.assertTrue(self.stdout_h.error_record_filter(self.log_info))
        self.assertTrue(self.stdout_h.error_record_filter(self.log_warning))

    def test_stdout_handlers_false(self):
        self.assertFalse(self.stdout_h.error_record_filter(self.log_error))
        self.assertFalse(self.stdout_h.error_record_filter(self.log_critical))

    def test_stderr_handlers_true(self):
        self.assertTrue(self.stderr_h.error_record_filter(self.log_error))
        self.assertTrue(self.stderr_h.error_record_filter(self.log_critical))

    def test_stderr_handlers_false(self):
        self.assertFalse(self.stderr_h.error_record_filter(self.log_debug))
        self.assertFalse(self.stderr_h.error_record_filter(self.log_info))
        self.assertFalse(self.stderr_h.error_record_filter(self.log_warning))


if __name__ == '__main__':
    unittest.main()
