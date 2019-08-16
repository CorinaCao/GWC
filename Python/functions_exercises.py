def is_even(num):
    if (num % 2 == 0):
        return True
    else:
        return False
is_even(6)
print(is_even(6))
print(is_even(11))
print(is_even(20))
print(is_even(61))

list = [1, 12, 21, 3, 45]
def calc_total(num):
    number = sum(num)
    print(number)
calc_total(list)
