import time


def now():
    return time.time() * 1000.0


start = now()
optimise = True
list_primes = []


def is_number_prime(the_number_to_check):
    is_prime = True
    if optimise:
        # justin says this is faster
        nums_to_divide_by = list_primes
    else:
        # Im staring with the no.2, because we already know that no.1 isn't prime, because it can only divided by itself
        nums_to_divide_by = range(2, the_number_to_check)

    for number_to_divide_by in nums_to_divide_by:
        # use modulo to see if there is a remainder.
        # if the remainder is zero, then the number is NOT prime
        if the_number_to_check % number_to_divide_by == 0:
            is_prime = False
            break  # no need to continue checking all the other numbers
    return is_prime


########################################################################################################################
# assume the number is prime. if its got a remainder after being divided by something, then its not prime
for number_to_check in range(2, 10000):
    the_number_is_prime = is_number_prime(number_to_check)

    if the_number_is_prime:
        list_primes.append(number_to_check)


print("Here are the prime numbers:")
print(list_primes)
print("Took %d milliseconds" % (now() - start))
