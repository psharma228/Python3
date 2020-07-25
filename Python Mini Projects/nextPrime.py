
# Script to generate prime numbers
# until the user chooses to stop 


#function to check if the number is prime
def isPrime(num):

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True


#funtion to generate prime number
def genPrime(primeNum):

    nextPrime = primeNum + 1

    while True:

        if not isPrime(nextPrime):
            nextPrime += 1

        else:
            break
    return nextPrime

#MAIN function starts here
def main(): 

	#starat with the first prime number
    primeNum = 2

    while True:
        choice = input('Do you want to see the next prime number? (Y/N) ')

        if choice.lower().startswith('y'):
            print(primeNum)
            primeNum = genPrime(primeNum)

        else:
            break

if __name__ == '__main__':
    main()