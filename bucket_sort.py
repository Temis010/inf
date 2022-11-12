def insertion_sort(array):
            for i in range(1, len(array)):
                key = array[i]
                j = i-1
                while array[j] > key and j >= 0:
                    array[j+1] = array[j]
                    j -= 1
                array[j+1] = key
            return array

def sortirovka(n):
    # Находим максимальное значение в списке. Затем используем длину списка, чтобы определить, какое значение в списке попадет в какой блок
    max_value = max(n)
    size = max_value/len(n)

    # Создаем n пустых блоков, где n равно длине входного списка
    buckets_list= []
    for x in range(len(n)):
        buckets_list.append([]) 

    # Помещаем элементы списка в разные блоки на основе size
    for i in range(len(n)):
        j = int (n[i] / size)
        if j != len (n):
            buckets_list[j].append(n[i])
        else:
            buckets_list[len(n) - 1].append(n[i])

    # Сортируем элементы внутри блоков с помощью сортировки вставкой
    for z in range(len(n)):
        insertion_sort(n)
            
    # Объединяем блоки с отсортированными элементами в один список
    final_output = []
    for x in range(len (n)):
        final_output = final_output + buckets_list[x]
    return final_output
