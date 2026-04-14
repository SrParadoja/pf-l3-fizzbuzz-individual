for numeromisterioso in range(1, 1001):
    if numeromisterioso % 3 == 0 and numeromisterioso % 5 == 0:
        print("FizzBuzz")
    elif numeromisterioso % 3 == 0:
        print("Fizz")
    elif numeromisterioso % 5 == 0:
        print("Buzz")
    else:
        print(numeromisterioso)