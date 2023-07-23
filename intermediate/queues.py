import queue

q = queue.Queue()
numbers = [10,20,30,40,50,60,70,80,90]

for num in numbers:
    q.put(num)

print(q.get())

q = queue.LifoQueue()
numbers = [10,20,30,40,50,60,70,80,90]

for num in numbers:
    q.put(num)

print(q.get())

q = queue.PriorityQueue()

q.put((11,True))
q.put((1,"First Priority"))
q.put((4,"Forth Priority"))
q.put((2,"Second Priority"))

while not q.empty():
    print(q.get())

