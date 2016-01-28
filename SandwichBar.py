import unittest

#
# Assignment
#

# Note: this function name should be `which_order` (in snakecase) <https://www.python.org/dev/peps/pep-0008/>
def whichOrder(available, orders):
  # TODO: add your code here
  
  return(0) # Note: this method has been stubbed for the first test case, but it will fail the second test case
  
#
# Unit Tests
#

class Test(unittest.TestCase):
  # Note: test cases are methods that begin with `test` <https://docs.python.org/2/library/unittest.html>

  def test_example_1(self):
    available = ["ham", "cheese", "mustard"]
    order = ["ham cheese"]
    value = whichOrder(available, order)

    self.assertEqual(value, 0)

  def test_example_2(self):
    available = ["ham", "cheese", "mustard"]
    order = ["cheese ham", "cheese mustard lettuce", "ketchup", "beer"]
    value = whichOrder(available, order)

    self.assertEqual(value, 1)

  # TODO: add `test_example_3` and `test_example_4` from "Examples" <http://www.cs.duke.edu/csed/pythonapt/sandwichbar.html>

if __name__ == '__main__':
  unittest.main()
