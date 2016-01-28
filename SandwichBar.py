def which_order(available, orders):
  for index, order in enumerate(orders):
    if list(set(order.split(' '))^set(list(set(available)&set(order.split(' '))))) == []:
      return index

  return -1
