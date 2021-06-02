print("Введите последовательность через пробел")

# вводим последовательность
input_string = input()
An_list = input_string.split()
print("Последовательность ---")
print(An_list)

SumPositiveAfterZero = 0
flag = False
counterAfterZero = 0
for i in An_list:
    # AveragePositiveAfterZero += int(i)
    # counterAfterZero += 1
    if (int(i) == 0): flag = True
    if (flag == True):
        if (int(i)>0):
            SumPositiveAfterZero += int(i)
            counterAfterZero += 1
print("Summary Positive after zero =", SumPositiveAfterZero)
print("counter After Zero =", counterAfterZero)
print("среднее", SumPositiveAfterZero / counterAfterZero)
