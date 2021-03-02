for i in range(1,100):
    if i%3:
        print("Fizz")
        continue;
    elif i%5:
        print("Buzz")
        continue;
    elif i%3 and i%5:
        print("FizzBuzz")
        continue;
    else:
        print("none")
        break;