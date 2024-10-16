import unittest
from tests_12_3 import Tournament
from tests_12_2 import Runner


def skip_if_frozen(test_case):
    def wrapper(self, *args, **kwargs):
        if self.__class__.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            test_case(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        runner = Runner("Run Boy Run")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("Woodkid")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Le Monde")
        runner2 = Runner("Skyfall")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_race_usain_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == "Ник")

    @skip_if_frozen
    def test_race_andrey_and_nik(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == "Ник")

    @skip_if_frozen
    def test_race_usain_andrey_and_nik(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(self.all_results[max(self.all_results.keys())].name == "Ник")


suite = unittest.TestSuite()
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)