#!/usr/bin/python -t
# Joshua Pena

import sys

# + -
# This program factors one positive (b)  and one negative (c) number

def factor01(additionGoal, multiplyGoal):
  num1 = 0
  num2 = 0
  check = 0
  multiplyCheck = 0
  additionCheck = 0
  impossible = 0

  if (multiplyGoal < additionGoal):
    possibleCheck = additionGoal
  else:
    possibleCheck = multiplyGoal

  while (multiplyCheck != 1):
    while (additionCheck != 1):
      check = num1 + num2
      if (check < additionGoal):
        num1 += 1
      elif (num2 < -possibleCheck):
        impossible = 1
        additionCheck = 1
      elif (check > additionGoal):
        num1 = 0
        num2 -= 1
      elif (check == additionGoal):
        additionCheck = 1
    check = num1 * num2
    if (check == multiplyGoal):
      multiplyCheck = 1
    else:
      additionCheck = 0
      num1 = 0
      num2 -= 1
    if (impossible == 1):
      multiplyCheck = 1

  if (impossible == 0):
    print "(x + %d) (x - %d)" % (num1, -num2)
  else:
    print "Not Possible"
