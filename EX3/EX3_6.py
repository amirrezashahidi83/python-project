def EX3_6(numbers):
    largest = 0
    smallest = 0
    for i in range(0,len(numbers) - 1):
        if numbers[i] < numbers[i+1]:
            largest = numbers[i+1]
        elif numbers[i] > numbers[i+1]:
            smallest = numbers[i+1]

    hasit = (largest - smallest) in numbers
    if hasit:
        return ":)"
    else:
        return ":("
    return ":/"
