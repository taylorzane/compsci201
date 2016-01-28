#!/usr/bin/python

import unittest

from SandwichBar import which_order

class Test(unittest.TestCase):
  # Note: test cases are methods that begin with `test` <https://docs.python.org/2/library/unittest.html>
  def test_example_1(self):
    available = ["ham", "cheese", "mustard"]
    order = ["ham cheese"]
    value = which_order(available, order)

    self.assertEqual(value, 0)

  def test_example_2(self):
    available = ["cheese", "mustard", "lettuce"]
    order = ["cheese ham", "cheese mustard lettuce", "ketchup", "beer"]
    value = which_order(available, order)

    self.assertEqual(value, 1)

  def test_example_3(self):
    available = [ "cheese", "cheese", "cheese", "tomato" ]
    order = [ "ham ham ham", "water", "pork", "bread", "cheese tomato cheese", "beef" ]
    value = which_order(available, order)

    self.assertEqual(value, 4)

  def test_example_4(self):
    available = [ "foo", "bar", "baz", "gazonk", "quux", "bat", "xyzzy", "shme", "hukarz", "grault", "waldo", "bleh" ]
    order = [ "kalatehas", "spam eggs", "needle haystack", "bleh blarg", "plugh", "the best sandwich in the universe" ]
    value = which_order(available, order)

    self.assertEqual(value, -1)

if __name__ == "__main__":
  unittest.main()
