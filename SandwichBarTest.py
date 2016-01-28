import unittest
from SandwichBar import whichOrder

class Test(unittest.TestCase):
  # Note: test cases are methods that begin with `test` <https://docs.python.org/2/library/unittest.html>

  def test_example_1(self):
    available = ["ham", "cheese", "mustard"]
    order = ["ham cheese"]
    value = whichOrder(available, order)

    self.assertEqual(value, 0)

  def test_example_2(self):
    available = ["cheese", "mustard", "lettuce"]
    order = ["cheese ham", "cheese mustard lettuce", "ketchup", "beer"]
    value = whichOrder(available, order)

    self.assertEqual(value, 1)

  # TODO: add `test_example_3` and `test_example_4` from "Examples" <http://www.cs.duke.edu/csed/pythonapt/sandwichbar.html>

if __name__ == "__main__":
  unittest.main()
