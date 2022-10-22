def EX1_1(number):
    return number + 1

def EX1_2(base,height):
    return base * height / 2

def EX1_3(side1,side2):
    maximum = side1 + side2 
    return maximum

def EX1_4(index):
    if index == 1:
        return "Monday"
    elif index == 2:
        return "Tuesday"
    elif index == 3:
        return "Wednesday"
    elif index == 4:
        return "Thursday"
    elif index == 5:
        return "Friday"
    elif index == 6:
        return "Satuarday"
    elif index == 7:
        return "Sunday"

def EX1_5(age):
    if age <= 1:
        return "Intant"
    elif age > 1 and age < 13:
        return "Child"
    elif age >= 13 and age < 20:
        return "Teenager"
    elif age >= 20:
        return "Adult"

def EX1_6(num):
    if num == 1:
        return "I"
    elif num == 2:
        return "II"
    elif num == 3:
        return "III"
    elif num == 4:
        return "IV"
    elif num == 5:
        return "V"
    elif num == 6:
        return "VI"
    elif num == 7:
        return "VII"
    elif num == 8:
        return "VIII"
    elif num == 9:
        return "IX"
    elif num == 10:
        return "X"
    else:
        return "Error: Outside number"
