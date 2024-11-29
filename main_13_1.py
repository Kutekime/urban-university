import asyncio

async def start_strongman(name, power): #где name - имя силача, power - его подъёмная мощность.
    print(f'Силач {name} начал соревнования.')
    balls = 5 #количество шаров

    for ball in range(balls):
        await asyncio.sleep(10/power)
        print(f'Силач {name} поднял {ball + 1}')

    print(f'Силач {name} закончил соревнования.')

async def start_tournament(): #в которой создаются 3 задачи для функций start_strongman.
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())
