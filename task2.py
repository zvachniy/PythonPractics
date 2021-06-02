print("Введите последовательность через пробел")
# x = input()
# p = input()
# вводим последовательность

input_string = input()
# An_list = [x * int(p) for x in range(10)]
An_list = input_string.split()
print("Последовательность ---")
print(An_list)

print("Введите минимальный элемент")
p_min = input()
print("Введите максимальный элемент")
p_max = input()
sum = 0
for i in An_list[int(p_min):int(p_max):2]:
    sum += int(i)
print("Сумма чётных элементов = ", sum)
