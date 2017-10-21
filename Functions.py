def is_number_prime(number_to_check):
    is_prime = True
    # I'm staring with the no.2, because we already know that no.1 isn't prime, because it can only divided by itself
    for numberToDivideBy in range(2, number_to_check):
        # use modulo to see if there is a remainder.
        # if the remainder is zero, then the number is NOT prime
        if number_to_check % numberToDivideBy == 0:
            is_prime = False
            break  # no need to continue checking all the other numbers
    return is_prime


########################################################################################################################
# assume the number is prime. if its got a remainder after being divided by something, then its not prime
for numberToCheck in range(1, 10000):
    the_number_is_prime = is_number_prime(numberToCheck)

    if the_number_is_prime:
        print("%d is prime" % numberToCheck)
