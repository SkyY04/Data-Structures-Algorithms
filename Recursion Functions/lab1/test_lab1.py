import unittest
from lab1 import wins_rock_scissors_paper, factorial, fibonacci, sum_to_goal, UpCounter, DownCounter

class MyLab1Tests(unittest.TestCase):
    """Personal test suite for validating lab1 implementations."""

    def test_rps_logic(self):
        # Rock beats Scissors
        self.assertTrue(wins_rock_scissors_paper("ROCK", "scissors"))
        # Scissors lose to Rock
        self.assertFalse(wins_rock_scissors_paper("scissors", "rock"))
        # Paper vs Paper should not win
        self.assertFalse(wins_rock_scissors_paper("Paper", "paper"))
        # Mixed casing and spaces
        self.assertTrue(wins_rock_scissors_paper("Paper", "rock"))
        self.assertFalse(wins_rock_scissors_paper("rock", "ROCK"))
        self.assertTrue(wins_rock_scissors_paper("scissors", "paper"))

    def test_factorial_values(self):
        self.assertEqual(factorial(0), 1)  # edge case
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(3), 6)

    def test_fibonacci_sequence(self):
        # Testing a few numbers from the Fibonacci sequence
        fib_values = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i, val in enumerate(fib_values):
            self.assertEqual(fibonacci(i), val)

    def test_sum_until_goal(self):
        test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sum_to_goal(test_data, 5), 15)  # 1+2+3+4+5
        self.assertEqual(sum_to_goal(test_data, 0), 0)  # no additions
        self.assertEqual(sum_to_goal(test_data, 11), 55)  # only numbers <= 10

    def test_up_counter_functionality(self):
        up = UpCounter(2)
        self.assertEqual(up.count(), 0)
        up.update()
        self.assertEqual(up.count(), 2)
        up.update()
        self.assertEqual(up.count(), 4)
        up.update()
        self.assertEqual(up.count(), 6)

    def test_down_counter_behavior(self):
        down = DownCounter(4)
        down.update()
        down.update()
        self.assertEqual(down.count(), -8)
        down.update()
        self.assertEqual(down.count(), -12)

if __name__ == '__main__':
    unittest.main()
