import random

# 1

def get_lucky_numbers(amount: int) -> tuple[int]:
    l1 = []
    for i in range(amount):
        l1.append(random.randint(1, 100))
    return tuple(l1)

print(get_lucky_numbers(5))

# 2

def input_until_lucky(lucky_numbers: tuple) -> int:
    i = 0
    while True:
        try:
            guess = int(input('guess a lucky number: '))
            i += 1
        except ValueError:
            print('invalid input. try again')
            continue
        if int(guess) in lucky_numbers:
            return i


tup1 = (3, 6, 10, 20, 56)

print(input_until_lucky(tup1))

##


