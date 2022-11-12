import timeit
import fast_sort
a = list(map(int,input('Введите числа массива:'). split()))
f = fast_sort.q(a)
print(f)

endtime =timeit.timeit()
print('Время выполнения программы: ', endtime)


import comb_sort
a = list(map(int,input('Введите числа массива:'). split()))
f = comb_sort.comb(a)
print('Результат сортировки', f)

etime = timeit.timeit()
print('Время выполнения программы: ',etime)
