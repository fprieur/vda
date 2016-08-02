import unittest
from ports.ports import Ports


class TestRetournePort(unittest.TestCase):
    def test(self):
        p = Ports()
        self.assertEqual(p.ports(), "80")

if __name__ == '__main__':
    unittest.main()
