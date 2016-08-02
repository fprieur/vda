import unittest
from ports.ports import Ports


class TestRetournePort(unittest.TestCase):
    def test(self):
        p = Ports()
        self.assertEqual(p.ports(), "81 80 50001")

if __name__ == '__main__':
    unittest.main()
