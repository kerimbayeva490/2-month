def bubble_sort(bubble):
    n = len(bubble)
    while bubble != sorted(bubble):
        for i in range(0, n-1):
            if bubble[i] > bubble[i+1]:
                bubble[i], bubble[i+1] = bubble[i+1], bubble[i]


bubble = [13, 3, 56, 0, 71, 96, 35, 8, 9, 27, 48, 82]
bubble_sort(bubble)
bubble_list = bubble
print(bubble_list)


from random import randint

def binary_search(val):
    n = 5000
    resultOk = False
    first = 0
    last = n - 1
    while first < last:
        middle = (first + last) // 2
        if val == middle:
            first = middle
            last = first
            resultOk = True
            pos = middle
        else:
            if val < middle:
                first = middle + 1
            else:
                last = middle - 1

    if resultOk == True:
        print("Элемент найден")
        print(pos)
    else:
        print("Элемент не найден")

val = randint(0, 5000)
print(val)
binary_search(val)