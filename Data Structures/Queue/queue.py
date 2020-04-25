class Queue:

    def __init__(self):

        self.queue = []

    def enqueue(self, item):

        self.queue.append(item)

    def dequeue(self):
        
        self.queue.remove(self.queue[0])

    def peak(self):

        return self.queue[0]

    def is_empty(self):

        return len(self.queue) == 0

    def print(self):

        for item in self.queue:

            print(item)
    


queue = Queue()

print(queue.is_empty())

queue.enqueue('1')
queue.enqueue('2')
queue.print()
queue.dequeue()
queue.print()

print(queue.is_empty())