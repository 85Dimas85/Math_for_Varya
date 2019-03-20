import random


def shuffle_machine(array):
    random.shuffle(array)
    return array


def action(x, act, y):
    actions = {
        '+': x + y,
        '-': x - y,
        '*': x * y,
        '/': x / y
    }
    if act in actions:
        actions_result = actions[act]
    return actions_result


def main():
    # Generate numbers
    a = []
    for I in range(4):
        a.append(random.randint(1, 100))

    # mix numbers and signs
    sign = ['+', '-', '*', '/']
    shuffle_machine(sign)

    # Replace '/' sign with '+' if it is the first element of array.
    if sign[0] == '/':
        sign[0] = '+'

    element = []
    for I in range(4):
        element.append(a[I])
        element.append(sign[I])
    element = element[:-1]
    print("initial\t\t\t\t", element)
    for j in range(element.__len__()-1):
        # Change neighbors elements near '-', to make left element grater than right
        if element[j] == '-':
            if element[j-1] < element[j+1]:
                tmp_element = element[j+1]
                element[j+1] = element[j-1]
                element[j-1] = tmp_element
    print("after '-' changes\t", element)

    # Change element after '/' sign to [2-10]
    # It should make calculations more easy, avoiding division on big numbers
    # Left element will divide by right
    for j in range(element.__len__() - 1):
        if element[j] == '/':
            element[j+1] = (random.randint(2, 10))
            element[j-1] = (random.randint(2, 10) * element[j+1])
    print("after '/' changes\t", element, 'and range element=', range(element.__len__()))

    # Change element after '*' sign to [2-10]
    # It should make calculations more easy, avoiding multiplication on big numbers
    for j in range(element.__len__() - 1):
        if element[j] == '*':
            element[j+1] = (random.randint(2, 10))
    print("after '*' changes\t", element)

    # Start interaction with user
    print("Calculate result:", element[0], element[1], "(", element[2],
          element[3], element[4], ")", element[5], element[6])
    # print("Give result in result.00 format if it will be float")

    # First action in the brackets
    first_action = action(element[2], element[3], element[4])

    # Define the second action. Based on sign
    HighPriorySigns = ['*', '/']
    if element[1] in HighPriorySigns:
        second_action = action(element[0], element[1], first_action)
        result = action(second_action, element[5], element[6])
    else:
        second_action = action(first_action, element[5], element[6])
        result = action(element[0], element[1], second_action)

    # Get and check result from user
    # Format it in float.00 format
    IncomingResult = format(float(input('Result:')), '.2f')
    if IncomingResult == format(result, '.2f'):
        print("You are right")
    else:
        print("You are wrong")
        print("First action result is:", first_action)
        print("Second action result is:", second_action)
        print("Right result is:", format(result, '.2f'))


while True:
    try:
        ExercisesNumber = int(input('How many exercises do you want to do?'))
        # ExercisesNumber = 5
        for i in range(ExercisesNumber):
            main()
            print()
            print()
        break
    except ValueError:
        print("It should be integer")

