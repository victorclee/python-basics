def get_stats(sequence):
  """
  The function `get_stats` takes a sequence of numbers as input and returns the maximum and minimum
  values in the sequence.
  
  :param sequence: The `sequence` parameter in the `get_stats` function is a tuple of numbers. In this
  case, the `numbers` tuple contains the values (1, 2, 3)
  :return: The `get_stats` function returns the maximum and minimum values from the input sequence.
  """
  return max(sequence), min(sequence)
  
numbers = (1, 2, 3)

maximum, minimum = get_stats(numbers)

print(maximum)
print(minimum)
