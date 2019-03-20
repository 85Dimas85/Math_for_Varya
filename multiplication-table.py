import random


def my_shuffle(array):
    random.shuffle(array)
    return array


def shuffle_nums(count):
    multi = []
    j = 2
    while j <= 9:
        for i in range(count // 8):
            multi.append(j)
        j += 1

    j = 2
    for simple in range(count % 8):
        multi.append(j)
        j += 1
    multi = my_shuffle(multi)
    return multi


def multiplication(a, b):
    print(a, '*', b, '=', end='', sep='')
    incoming = int(input())
    if incoming == (a * b):
        print('+')
        return correct.append(a)
    else:
        print('-')
        return error.append(a)


exercises_count = int(input("How many exercises do you want to do?"))
exercises_base = int(input("Multiplication for which number do you want to train?"))
correct = []
error = []

shuffle_list = shuffle_nums(exercises_count)

for i in range(exercises_count):
    multiplication(shuffle_list[i], exercises_base)
    # print("correct", correct)

print("error", error)
print("Work on errors")

while error.__len__() > 0:
    shuffle_list = error
    error = []
    correct = []

    for i in range(shuffle_list.__len__()):
        multiplication(shuffle_list[i], exercises_base)
        # print("correct", correct)
    print("error", error)




