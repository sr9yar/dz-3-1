test_cases = [
    {
      "from_arg": 1,
      "to_arg": 3
    },
    {
      "from_arg": 5,
      "to_arg": 7
    },
    {
      "from_arg": 1,
      "to_arg": 100
    }
  ] 



def sum_distance(from_arg, to_arg) -> int:
  if from_arg > to_arg:
    r = range(to_arg, from_arg+1)
  else:
    r = range(from_arg, to_arg+1)

  result = 0

  for number in r:
    result += number

  return result



def main() -> None:
  for test_case in test_cases:
    sum = sum_distance(test_case["from_arg"], test_case["to_arg"])
    print(f"Результат для аргументов {test_case["from_arg"]}, {test_case["to_arg"]}: {sum}")




main()
