import unittest
from ports.ports import Ports


class TestRetournePort(unittest.TestCase):
    def test(self):
        p = Ports()
        self.assertEqual(p.ports(), "50001 81 80")

    def testNotEmptyPorts(self):
        p = Ports()
        self.assertIsNot(p.ports(), "", "la fonction port ne retourne pas rien")

if __name__ == '__main__':
    unittest.main()
