import threading
import time

# event = threading.Event()

# def my_func():
#     print("waiting for event to trigger.....\n")
#     event.wait()
#     print("Event is triggered!!")

# t1 = threading.Thread(target=my_func)
# t1.start()

# x = input("Do you want to trigger the event (y/n)?\n")
# if x=="y":
#     event.set()


path = "text.txt"

text = ""

def read_file():
    global path, text
    while True:
        with open("text.txt", "r") as f:
            text = f.read()
        time.sleep(3)


def print_loop():
    for x in range(30):
        print(text,x)
        time.sleep(1)


t1 = threading.Thread(target=read_file,daemon=True)
t2 = threading.Thread(target=print_loop)

t1.start()
t2.start()


