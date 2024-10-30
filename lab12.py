def display_digits(number):
    print("Цифри числа у стовпчик:")
    for digit in str(number):
        print(digit)
    print("Цифри числа у порядку спадання:")
    for digit in sorted(str(number), reverse=True):
        print(digit)
number = int(input("Введіть натуральне число: "))
display_digits(number)