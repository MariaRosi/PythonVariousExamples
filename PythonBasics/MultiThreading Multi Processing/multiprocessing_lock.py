import multiprocessing
import time

def deposit(balance, lock):
    for i in range(10):
        time.sleep(1)
        lock.acquire()
        balance.value = balance.value + 1
        print('Inside deposit',balance.value)
        lock.release()

def withdraw(balance, lock):
    for i in range(10):
        time.sleep(1)
        lock.acquire()
        balance.value = balance.value - 1
        print('Inside withdraw',balance.value)
        lock.release()

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 300)
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=deposit, args=(balance,lock))
    p2 = multiprocessing.Process(target=withdraw, args=(balance, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Inside main process',balance.value)
