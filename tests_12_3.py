#runner
class Runner:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def __eq__(self, other):
        return self.name == other.name

    def run(self, distance):
        self.distance += distance * self.speed

    def walk(self, distance):
        self.distance += distance * (self.speed / 2)


class Tournament:
    def __init__(self, distance, participants):
        self.distance = distance
        self.participants = participants

    def start(self):
        results = {}
        for participant in self.participants:
            participant.run(self.distance)
            results[participant.distance] = participant.name
        # Сортируем результаты по дистанции
        sorted_results = {i+1: results[key] for i, key in enumerate(sorted(results.keys(), reverse=True))}
        return sorted_results



#тесты
#runner.test
import unittest
from runner import Runner

def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.runner = Runner(name="TestRunner", speed=5)

    @skip_if_frozen
    def test_run(self):
        self.runner.run(10)
        self.assertEqual(self.runner.distance, 50)

    @skip_if_frozen
    def test_walk(self):
        self.runner.walk(10)
        self.assertEqual(self.runner.distance, 25)

    @skip_if_frozen
    def test_challenge(self):
        self.runner.run(20)
        self.assertEqual(self.runner.distance, 100)



#tournament.test
import unittest
from runner import Runner
from tournament import Tournament

def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func(self, *args, **kwargs)
    return wrapper

class TournamentTest(unittest.TestCase):
    is_frozen = True
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner(name="Усэйн", speed=10)
        self.andrey = Runner(name="Андрей", speed=9)
        self.nick = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    @skip_if_frozen
    def test_usain_and_nick(self):
        tournament = Tournament(distance=90, participants=[self.usain, self.nick])
        result = tournament.start()
        self.all_results[1] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @skip_if_frozen
    def test_andrey_and_nick(self):
        tournament = Tournament(distance=90, participants=[self.andrey, self.nick])
        result = tournament.start()
        self.all_results[2] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @skip_if_frozen
    def test_usain_andrey_and_nick(self):
        tournament = Tournament(distance=90, participants=[self.usain, self.andrey, self.nick])
        result = tournament.start()
        self.all_results[3] = result
        self.assertTrue(result[max(result.keys())] == "Ник")

    @skip_if_frozen
    def test_sorted_results(self):
        tournament = Tournament(distance=90, participants=[self.usain, self.andrey, self.nick])
        result = tournament.start()
        self.all_results[4] = result
        self.assertTrue(result[1] == "Усэйн")
        self.assertTrue(result[2] == "Андрей")
        self.assertTrue(result[3] == "Ник")
