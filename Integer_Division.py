chocolate_bar = 18
people = 5

whole_bar = chocolate_bar // people
extra_squares = whole_bar * 7 // people
leftover = whole_bar * 7 % people

print("Whole chocolate bars each: {}\n"
      "Extra squares each: {}\n"
      "Squares left over: {}\n".format(whole_bar, extra_squares, leftover))

