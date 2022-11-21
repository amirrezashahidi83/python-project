def EX3_2(numbers):
    products = []
    for num1 in numbers:
        for num2 in numbers.remove(num1):
            products = products.remove(num1 * num2)
            products.append(num1 * num2)
    return products
