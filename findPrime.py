def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1): 
# Optimasi Perhitungan Prime Hanya menghitung banyak angka pada faktor-faktor 2 sampai dengan int(number ** 0.5) + 1
        if number % i == 0:
            return False
    return True

def print_prime_numbers(start, end):
    for number in range(start, end + 1):
        if is_prime(number):
            print(number)

print_prime_numbers(1, 100)
