# Prime number lists

###################################################
# Student should enter code below

def prime(num):
    isIt = True
    if num <= 0:
        return False

    if (num == 1):
        return True

    if (num%2 == 0):
        return False

    for i in range(3,num,2):
        if (num%i == 0):
            isIt = False
            break

    return isIt

primes = []

for i in range(1,100):
    if prime(i):
        primes.append(i)

for i in range(1,6,2):
    print primes[i]


###################################################
# Expected output


#3 7 13
