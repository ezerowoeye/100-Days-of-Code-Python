# 1 : Prime numbers using functions and modules:
def prime_checker(number):
    is_prime = False
    for i in range(2, number):
        if number % i == 0:
            is_prime = True
    if is_prime:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
