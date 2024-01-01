# Prime Number Checker

def prime_checker(number):
    prime = False
    if number == 1:
        print("It's not a prime number.")
    elif number > 1:
        for i in range(2, number):
            if number % i == 0:
                prime = True
                break
        if prime == True:
            print("It's not a prime number.")
        elif prime == False:
            print("It's a prime number.")
        
n = int(input()) # Check this number

prime_checker(number=n)