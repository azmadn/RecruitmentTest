def multiply(x, y):
    total = 0
    temp = x
    while temp != 0:
        total += y
        if temp < 0 :
            temp += 1
        else :
            temp -= 1
    
    if (x < 0 and y > 0) or ( x < 0 and y < 0):
        return -total
    else:
        return total
    
# testing function
# jika nilai x dan y positif
print(multiply(5,7))
print(multiply(3,7))

# jika nilai x atau y bernilai negatif
print(multiply(-3,5))
print(multiply(3,-5))

#jika nilai (x atau y) = 0
print(multiply(0,10))
print(multiply(7,0))

#jika nilai x dan y negatif
print(multiply(-4,-6))

#angka besar
print(multiply(1232, 1234))




