import threading
import time

def write_words(word_count, file_name):
    __started_at = time.time()
    with  open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write('Cowabunga! № ' + str(i) + '\n')
            time.sleep(0.1)
        file.write(f'Завершилась запись в файл {file_name}')
        __ended_at = time.time()
        print(f'Завершилась запись в файл {file_name}\n Затраченное время: {(__ended_at - __started_at).__round__(2)}')

started_at_global=time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
ended_at__global=time.time()
print(f'Завершилась запись в первые четыре файла {(ended_at__global - started_at_global).__round__(2)}')
print()

started_at_global=time.time()
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
#thread1.start()
#thread1.join()
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
#thread2.start()
#thread2.join()
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
#thread3.start()
#thread3.join()
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Ждем завершения всех потоков
thread1.join()
thread2.join()
thread3.join()
thread4.join()
ended_at__global=time.time()
print(f'Завершилась запись в последние четыре файла {(ended_at__global - started_at_global).__round__(2)}') #Эта
# строчка почему-то не выводится!
# "Ждем завершения всех потоков" Такое решение мне подсказал ИИ. Теперь всё работает!
# А то я сначала делал "тупо" как в лекции (оставил закомментированным)

'''
Мой получившийся вывод в консоль:

Завершилась запись в файл example1.txt
 Затраченное время: 1.09
Завершилась запись в файл example2.txt
 Затраченное время: 3.27
Завершилась запись в файл example3.txt
 Затраченное время: 21.86
Завершилась запись в файл example4.txt
 Затраченное время: 10.87
Завершилась запись в первые четыре файла 37.1

Завершилась запись в файл example5.txt
 Затраченное время: 1.09
Завершилась запись в файл example6.txt
 Затраченное время: 3.25
Завершилась запись в файл example8.txt
 Затраченное время: 10.88
Завершилась запись в файл example7.txt
 Затраченное время: 21.77
Завершилась запись в последние четыре файла 21.77
'''