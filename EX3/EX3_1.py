def EX3_1(num):
    steps = 0
    current = num
    while current > 1:
        if current % 2 == 0:
            current = current / 2
        else:
            current = current * 3 + 1
    return steps
