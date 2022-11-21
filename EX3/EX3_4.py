def EX3_4(a,b,c):
    result = a
    for i in range(0,b):
        result += result
    return result % c == 0
