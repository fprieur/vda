import unittest
import agent as agent


class TestRetournePort(unittest.TestCase):
    def test(self):
        self.assertEqual(agent.ports(), "5000 80 8081")

if __name__ == '__main__':
    unittest.main()
