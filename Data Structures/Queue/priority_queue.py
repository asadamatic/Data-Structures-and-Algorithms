class Item:

    def __init__(self, data, priority):

        self.data = data
        self.priority = priority


class PriorityQueue:

    def __init__(self):

        self.priority_queue = []

    def enqueue(self, data, priority):

        item = Item(data, priority)
        self.priority_queue.append(item)

    def remove_highest_priority_item(self):

        self.priority_list = [item.priority for item in self.priority_queue]
        index = self.priority_list.index(max(self.priority_list))

        self.priority_queue.remove(self.priority_queue[index])
        
    def get_highest_priority_item(self):

        self.priority_list = [item.priority for item in self.priority_queue]
        index = self.priority_list.index(max(self.priority_list))

        return self.priority_queue[index].data

    def print(self):

        data_list = [item.data for item in self.priority_queue]
        
        for data in data_list:

            print(data)


queue = PriorityQueue()

queue.enqueue(1, 2)
queue.enqueue(3, 4)
queue.enqueue(4, 4)

queue.print()

print(queue.get_highest_priority_item())
queue.remove_highest_priority_item()

queue.print()


