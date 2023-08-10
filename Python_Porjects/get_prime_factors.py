factors=[]
def get_prime_factors(number):
    divisor=2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number//divisor
        else:
            divisor+=1
    return factors
num = int(input("enter a number: "))
prime_factors=get_prime_factors(num)
if len(prime_factors) > 1:
   grammar="are"
else:
    grammar="is"
print("Prime factors for the number {} that you entered {}: ".format(num,grammar),prime_factors)
