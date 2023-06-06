import asyncio
import sys

SCRIPTS = ['1.6.5.py',  '1.6.7.py',  '1.6.8.py',  '1.6.11.py',  '2.1.2.py',  '2.1.7.py',  '2.2.3.py',  '2.2.5.py',  '2.2.6.py']
async def waiter(sc, p):
    "Функция которая вернет имя скрипта после ожидания"
    await p.wait()
    return sc, p


async def main():
    waiters  = []
    
    # Запуск
    for sc in SCRIPTS:
        p = await asyncio.create_subprocess_exec(sys.executable, sc)
        print('Started', sc)
        waiters.append(asyncio.create_task(waiter(sc, p)))

    # Ожидание
    while waiters:
        done, waiters = await asyncio.wait(waiters, return_when=asyncio.FIRST_COMPLETED)
        for w in done:
            sc,p = await w
            print('Done', sc)
        
      
if __name__ == "__main__":
    asyncio.run(main())