##### ДЗ. Тема 4. Алгоритми сортування



### Завдання 1

'''
Python має дві вбудовані функції сортування: sorted і sort. Функції сортування Python використовують Timsort — гібридний алгоритм сортування, що поєднує в собі сортування злиттям і сортування вставками.

Порівняйте три алгоритми сортування: злиттям, вставками та Timsort за часом виконання. Аналіз повинен бути підтверджений емпіричними даними, отриманими шляхом тестування алгоритмів на різних наборах даних. Емпірично перевірте теоретичні оцінки складності алгоритмів, наприклад, сортуванням на великих масивах. Для заміру часу виконання алгоритмів використовуйте модуль timeit.

Покажіть, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим, і саме з цієї причини програмісти, в більшості випадків, використовують вбудовані в Python алгоритми, а не кодують самі. Зробіть висновки.


Критерії прийняття:

Виконано порівняльний аналіз алгоритмів за часом виконання шляхом їх тестування на різних наборах даних.
Емпірично перевірено теоретичні оцінки складності алгоритмів та доведено, що поєднання сортування злиттям і сортування вставками робить алгоритм Timsort набагато ефективнішим.
Зроблено висновки щодо ефективності алгоритмів для даного випадку. Висновки оформлено у вигляді файлу readme.md до домашнього завдання.
'''

import timeit
import random


# insertion_sort()
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

numbers = [5, 3, 8, 4, 2]
insertion_sort(numbers)


# merge_sort()

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


# Замір часу виконання алгоритму

def measure_time(sort_func, data):
    start_time = timeit.default_timer()
    sorted_data = sort_func(data[:]) # сортуємо не сам масив даних, а його копію, щоб початковий масив даних залишався незмінним при використанні інших методів сортування
    end_time = timeit.default_timer() - start_time
    return end_time

# Тестові дані
data_sample_1 = [random.randint(0, 1000) for _ in range(100)]
data_sample_2 = [random.randint(0, 1000) for _ in range(1000)]
data_sample_3 = [random.randint(0, 1000) for _ in range(10000)]


def main():
    for i in [data_sample_1, data_sample_2, data_sample_3]:
        length =  len(i)
        print(f'Sample of {length} elements\n')
        print(2*' ' + 'insertion_sort time:')
        print(4*' ' , measure_time(insertion_sort, i))
        print(2*' ' + 'merge_sort time:')
        print(4*' ' , measure_time(merge_sort, i))
        print(2*' ' + 'sorted time:')
        print(4*' ' , measure_time(sorted, i),'\n\n')
    

if __name__ == "__main__":
    main()


### Висновки
# Порівнявши емпіричним шляхом (на трьох різних вибірках) за часом виконання три алгоритми сортування: злиттям, вставками та Timsort (функція sorted),
# бачимо наступне: найменш ефективним алгоритмом сортування є сортування вставками (найбільша тривалість сортування), середнім за тривалістю виконання є алгоритм сортування злиттям, 
# а найбільш ефективним в даному випадку є алгоритм сортування Timsort — гібридний алгоритм сортування, що поєднує в собі сортування злиттям і сортування вставками.
# Адже бачимо, що зі збільшенням обсягу сортувального масиву, особливо на вибірці в 10000 елементів  відрив в часу розрахунку є суттєвим



'''
Sample of 100 elements

  insertion_sort time:
     0.00013020006008446217
  merge_sort time:
     0.00012620002962648869
  sorted time:
     9.200070053339005e-06 


Sample of 1000 elements

  insertion_sort time:
     0.01557180006057024
  merge_sort time:
     0.0013613998889923096
  sorted time:
     0.0001324999611824751


Sample of 10000 elements

  insertion_sort time:
     1.621315099997446
  merge_sort time:
     0.017173599917441607
  sorted time:
     0.0010840001050382853


'''


### Завдання 2 (необов'язкове)

'''
Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. 
При виконанні завдання можете опиратися на алгоритм сортування злиттям з конспекту. 
Реалізуйте функцію merge_k_lists , яка приймає на вхід список відсортованих списків та повертає відсортований список.

Приклад очікуваного результату:

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)


Виведення:

Відсортований список: [1, 1, 2, 3, 4, 4, 5, 6]
'''

def merge_k_lists(lists):
    # Об'єднуємо всі списки в один
    arr = []
    for i in lists:
        arr.extend(i)

    # Алгоритм merge sort
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        return merge(merge_sort(left_half), merge_sort(right_half))

    def merge(left, right):
        merged = []
        left_index = 0
        right_index = 0

        # Спочатку об'єднайте менші елементи
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        # Якщо в лівій або правій половині залишилися елементи, 
            # додайте їх до результату
        while left_index < len(left):
            merged.append(left[left_index])
            left_index += 1

        while right_index < len(right):
            merged.append(right[right_index])
            right_index += 1

        return merged

    # ВАЖЛИВО: повертаємо відсортований масив
    return merge_sort(arr)

# Тест
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
