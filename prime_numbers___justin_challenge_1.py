
# assume the number is prime. if its got a remainder after being divided by something, then its not prime
for numberToCheck in range(1, 10000):
    isPrime = True
    # I'm staring with the no.2, because we already know that no.1 isn't prime, because it can only divided by itself
    for numberToDivideBy in range(2, numberToCheck):
        # use modulo to see if there is a remainder.
        # if the remainder is zero, then the number is NOT prime
        if numberToCheck % numberToDivideBy == 0:
            isPrime = False
            break  # no need to continue checking all the other numbers!

    if isPrime:
        print("%d is prime" % numberToCheck)
    # else:
        # print("%d is not prime" % numberToCheck)

#                                ./
# I understood everything!      \/
# make it check all numbers up to 10000, not just one specific number
# add comments to show what you are trying to do
# try this max: https://www.tutorialspoint.com/python/python_functions.htm
