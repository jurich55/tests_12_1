import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_run(self):
        for run in range(10):
            return range
        self.assertEqual(self.distance, 100)

    def test_walk(self):
        for walk in range(10):
            return range
        self.assertEqual(self.distance, 50)

    def test_challenge(self):
        for walk in range(10):
            return walk
        for run in range(10):
            return  run
        self.assertNotEqual(distance)

if __name__ == '__main__':
    unittest.main()

