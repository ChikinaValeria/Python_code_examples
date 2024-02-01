# создаем список из введенной строки (разделитель -пробел)
given_list = input().split()

# кладем первый символ в новый список, удалив его из введенного списка
result_list = [[given_list.pop(0)]]

for el in given_list:
    # сравниваем элемент с последним элементом результирующего списка
    if el in result_list[-1]:
        result_list[-1].append(el)
    else:
        #
        result_list.append([el])

print(result_list)