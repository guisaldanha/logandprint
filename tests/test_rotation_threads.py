"""Concurrent rotation test. Run: python tests/test_rotation_threads.py"""
import glob
import os
import sys
import tempfile
import threading
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import logandprint as log
from logandprint import main as logmain

THREADS = 12
LINES = 300


def run_threads(path):
    errors, finished = [], []

    def worker(n):
        try:
            for i in range(LINES):
                log.write('T%02d-L%04d' % (n, i), console=False)
            finished.append(n)
        except BaseException as e:  # SystemExit included: threading swallows it silently
            errors.append((n, repr(e)))

    ts = [threading.Thread(target=worker, args=(n,)) for n in range(THREADS)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    logmain._closeFile()
    return errors, finished


class RotationThreads(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp()
        self.path = os.path.join(self.dir, 'x.log')
        log.setLogFile(self.path)
        log.setMaxFileSize(400)
        log.debugMode(False)

    def test_no_thread_dies(self):
        log.setBackupCount(3)
        errors, finished = run_threads(self.path)
        self.assertEqual(errors, [])
        self.assertEqual(len(finished), THREADS)

    def test_no_line_lost(self):
        log.setMaxFileSize(4000)
        log.setBackupCount(400)  # big enough that nothing is discarded
        errors, finished = run_threads(self.path)
        self.assertEqual(errors, [])
        self.assertEqual(len(finished), THREADS)
        lines = set()
        for f in glob.glob(self.path + '*'):
            with open(f, encoding='utf-8') as fh:
                for ln in fh:
                    lines.add(ln.rsplit(' - ', 1)[1].strip())
        expected = {'T%02d-L%04d' % (n, i) for n in range(THREADS) for i in range(LINES)}
        self.assertEqual(expected - lines, set())


if __name__ == '__main__':
    unittest.main()
