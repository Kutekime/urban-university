#import threading
import multiprocessing
import time
from concurrent.futures import ThreadPoolExecutor

def read_info(name):
    all_data = []
    __started_at = time.time()
    with  open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            # Обработка строки
            all_data.append(line)
        #а ещё, вроде можно делать for line in file как альтернатива (профи сказал, что это даже
        # более элегантное решение)
    __ended_at = time.time()
    print(f'Завершилось чтение файла {name}\n Затраченное время: {(__ended_at - __started_at).__round__(2)}')

#Этих операций достаточно, чтобы рассмотреть преимущество многопроцессного выполнения программы над линейным.
filenames_list =  [f'./file {number}.txt' for number in range(1, 5)] # ['file 1.txt', 'file 2.txt', 'file 3.txt',
# 'file 4.txt'] - сначала сделал просто, но раз есть пример списковой сборки - ок

# Линейный вызов
# with ThreadPoolExecutor(max_workers=4) as executor:
#     [executor.submit(read_info, filename) for filename in filenames_list]
    #results = [future.result() for future in futures] можно сделать, если сохранять результаты выполнения в futures,
    # а в методе есть return

# threading1 = threading.Thread(target=read_info, args=(filenames_list[0],))
# threading2 = threading.Thread(target=read_info, args=(filenames_list[1],))
# threading3 = threading.Thread(target=read_info, args=(filenames_list[2],))
# threading4 = threading.Thread(target=read_info, args=(filenames_list[3],))

# threading1.start()
# threading2.start()
# threading3.start()
# threading4.start()

#Многопроцессный
if __name__ == '__main__':
    start_time = time.perf_counter()

    with multiprocessing.Pool(processes=4) as pool: # Создание пула процессов
        pool.map(read_info, filenames_list)

    end_time = time.perf_counter()
    print(f'\nОбщее затраченное время {(end_time - start_time).__round__(2)}')
    print('Это время включает в себя:'
          '\n1. Время создания пула процессов.'
          '\n2. Время запуска всех процессов.'
          '\n3. Время ожидания завершения всех процессов и сбора результатов.')

    # process1 = multiprocessing.Process(target=read_info, args=(filenames_list[0],))
    # process2 = multiprocessing.Process(target=read_info, args=(filenames_list[1],))
    # process3 = multiprocessing.Process(target=read_info, args=(filenames_list[2],))
    # process4 = multiprocessing.Process(target=read_info, args=(filenames_list[3],))

    # process1.start()
    # process2.start()
    # process3.start()
    # process4.start()