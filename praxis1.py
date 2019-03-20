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


# Gentrate numbers
a = []
for i in range(4):
    a.append(random.randint(1, 100))

# mix numbers and signs
sign = ['+', '-', '*', '/']
#shuffle_machine(sign)
print(sign)
praxis = []
for i in range(4):
    praxis.append(a[i])
    praxis.append(sign[i])

# Start interaction with user
print("Calculate result:", praxis[0], praxis[1], "(", praxis[2], praxis[3], praxis[4], ")", praxis[5], praxis[6])
print("Give result in result.00 format if it will be float")

# First action in the buckets
first_action = action(praxis[2], praxis[3], praxis[4])

# Define the second action. Based on sign
HighPriorySigns = ['*', '/']
if praxis[1] in HighPriorySigns:
    second_action = action(praxis[0], praxis[1], first_action)
    result = action(second_action, praxis[5], praxis[6])
else:
    second_action = action(first_action, praxis[5], praxis[6])
    result = action(praxis[0], praxis[1], second_action)

# Get and check result from user
IncomingResult = format(float(input('Result:')), '.2f')
if IncomingResult == format(result, '.2f'):
    print("You are right")
else:
    print("You are wrong")
    print("First action result is:", first_action)
    print("Second action result is:", second_action)
    print("Right result is:", result)
