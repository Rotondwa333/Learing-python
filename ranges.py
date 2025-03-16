my_range = range(1,51)

def is_prime(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

for number in my_range:
    if is_prime(number):
        print(number)







