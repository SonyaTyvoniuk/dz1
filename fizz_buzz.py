def fizz_buzz(param):
    if param % 3 == 0: return "Fizz"
    if param % 5 == 0: return "Buzz"
    if param % 3 == 0 and number % 5 == 0: return "FizzBuzz"

    return str(param)

print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(4))