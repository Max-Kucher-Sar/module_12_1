import program
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        first_walk = program.Runner('Den')
        for _ in range(10):
            first_walk.walk()
        self.assertEqual(first_walk.distance, 50)

    def test_run(self):
        second_run = program.Runner('Max')
        for _ in range(10):
            second_run.run()
        self.assertEqual(second_run.distance, 100)

    def test_challenge(self):
        walker = program.Runner('Egor')
        runner = program.Runner('Vlad')
        for _ in range(10):
            walker.walk()
            runner.run()
        self.assertEqual(walker.distance, runner.distance)

