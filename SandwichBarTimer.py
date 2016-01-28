#!/usr/bin/python

import timeit

from SandwichBar import whichOrder

if __name__ == "__main__":
  setup = """\
from __main__ import whichOrder

available = ["cheese", "mustard", "lettuce"]
orders = ["cheese ham", "cheese mustard lettuce", "ketchup", "beer"]
"""

  print(timeit.timeit("whichOrder(available, orders)", setup))
