import threading
import time

# def loop():
#     n = 0
#     while n < 10:
#         print("N",n)
#         n += 1

# t1  =threading.Thread(target=loop)
# # to start thread
# t1.start() 
# # to wait for thread to finish and then execute next line
# t1.join()
# # t1.is_alive()

# Thread Locking
x = 8192
lock = threading.Lock()
def double() -> None:
    global x, lock
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached the max!",x)
    lock.release()


def halve() -> None:
    global x,lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    lock.release()



t1 =  threading.Thread(target=halve)
t2=  threading.Thread(target=double)
t1.start()
t2.start()


