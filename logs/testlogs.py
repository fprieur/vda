import unittest
from logs import Logs


class TestRetournePort(unittest.TestCase):
    def test(self):
        l = Logs()
        self.assertEqual(l.logsContainer, "henri", "test henri reussit")

if __name__ == '__main__':
    unittest.main()
