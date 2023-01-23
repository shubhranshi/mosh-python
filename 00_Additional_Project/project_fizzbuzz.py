# input number
# if number divisible by 3 - print fizz
# if number divisible by 5 - print buzz
# if number divisible by both 3 and 5 - print fizzbuzz

def fizzbuzz(input):
    if (input % 3) == 0 and (input % 5) == 0:
        return "fizzbuzz"
    elif (input % 3) == 0:
        return "fizz"
    elif (input % 5) == 0:
        return "buzz"
    return input


print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))
