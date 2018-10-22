import itertools

def crossout(numbers, prime):
    for number in numbers:
        if number % prime:
            yield number

def get_prime(numbers):
    while True:
        prime = next(numbers)
        numbers = crossout(numbers, prime)
        yield prime


list10 = list(itertools.islice(get_prime(itertools.count(2)), 10))
print(list10)

