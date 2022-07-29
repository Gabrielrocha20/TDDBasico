from calculadora import soma

# print(soma(10, 20))
# print(soma(-10, 20))
# print(soma(1.5, 2.5))

try:
    print(soma('10', 20))
except AssertionError as e:
    print('conta invalida')
    print(e)
